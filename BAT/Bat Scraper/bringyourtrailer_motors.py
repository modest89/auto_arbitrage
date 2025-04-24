import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import pandas as pd

# Set up Firefox options (optional, but recommended for headless mode)
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run in headless mode for faster performance

# Set up the Firefox driver
geckodriver_path = r"C:\tools\geckodriver\geckodriver.exe"
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

print("Starting script...")

def load_all_products(url, show_more_selector, max_products=None):
    print("Loading URL:", url)
    driver.get(url)
    
    # Allow time for the page to load
    time.sleep(3)
    print("Page loaded successfully.")

    products = []
    seen_products = set()  # Keep track of seen products
    prev_product_count = 0

    while max_products is None or len(products) < max_products:
        # Find all product elements
        product_elements = driver.find_elements(By.CSS_SELECTOR, 'a.listing-card')
        current_product_count = len(product_elements)
        print(f"Found {current_product_count} products on the current page.")

        # If no new products are loaded, break the loop
        if current_product_count == prev_product_count:
            break
        prev_product_count = current_product_count

        for index, product in enumerate(product_elements, start=1):
            try:
                title = product.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div:nth-child(1) > h3:nth-child(2)').text
            except NoSuchElementException:
                print(f"Title not found for product {index}")
                title = 'N/A'
            try:
                price = product.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div:nth-child(1) > div:nth-child(7)').text
            except NoSuchElementException:
                print(f"Price not found for product {index}")
                price = 'N/A'
            
            # Use the product title and price as a unique identifier
            product_id = (title, price)
            if product_id not in seen_products:
                seen_products.add(product_id)
                products.append({'title': title, 'price': price, 'category': 'motorcycles'})  # Store title, price, and category
            
            # Stop if we have collected enough products
            if max_products is not None and len(products) >= max_products:
                break

        if max_products is not None and len(products) >= max_products:
            break

        # Find and click the "Show More" button
        try:
            show_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, show_more_selector)))
            show_more_button.click()
            # Allow time for new products to load
            time.sleep(3)
            print("Clicked 'Show More' button.")
        except TimeoutException:
            print("No more products to load or error occurred: Show More button not found or not clickable.")
            break
        except NoSuchElementException:
            print("No more products to load or error occurred: Show More button not found.")
            break
        except Exception as e:
            print(f"No more products to load or error occurred: {e}")
            break

    return products

# URL of the page you want to scrape
url = 'https://bringatrailer.com/auctions/results/?category=70&yearFrom=1980&timeFrame=5Y&result=sold&bidTo=100000'

# CSS selector for the "Show More" button
show_more_selector = '.auctions-footer-button'  # Corrected CSS selector for the "Show More" button

print("Scraping data...")
# Load all products, you can set max_products=None for no limit
all_products = load_all_products(url, show_more_selector, max_products=None)  # No limit on the number of products

print("Data scraping complete. Saving to CSV...")

# Create a DataFrame
df = pd.DataFrame(all_products)

# Specify the folder path where you want to save the CSV file
folder_path = r"C:\Users\Modest\OneDrive\_With Modest (ONLY)\Various\Power Bi\BAT\Bat Data"

# Generate the filename with the current date
date_suffix = datetime.now().strftime("%m%d%Y")
output_filename = f"motor_{date_suffix}.csv"

# Combine the folder path and filename to create the full output file path
output_file_path = os.path.join(folder_path, output_filename)

# Save the DataFrame to CSV with the new file path
df.to_csv(output_file_path, index=False)

# Print a message confirming the file was saved successfully
print(f"CSV file saved successfully to: {output_file_path}")

# Close the browser
driver.quit()
print("Browser closed.")
