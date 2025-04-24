from Miner.AutoScout24Scraper import AutoScout24Scraper
import os


def main(scrape=False):
    # Define the list of make/model combinations
    make_model_combinations = [
        {"make": "volkswagen", "model": "golf-gti"},
        {"make": "volkswagen", "model": "golf-gtd"},
        {"make": "volkswagen", "model": "golf-gte"},
        {"make": "alfa-romeo", "model": "giulia"},
        {"make": "alfa-romeo", "model": "Giulietta"},
        {"make": "audi", "model": "rs4"},
        {"make": "bmw", "model": "128"},
        {"make": "bmw", "model": "135"},
        {"make": "volkswagen",  "model": "scirocco"}
    ]

    # Directly set zip_list to an empty list or a default value
    zip_list = ["default_zip_code"]  # Replace "default_zip_code" with an actual zip code if needed

    if scrape:
        for combination in make_model_combinations:
            make = combination["make"]
            model = combination["model"]
            scrape_autoscout(make, model, zip_list)


def scrape_autoscout(make, model, zip_list):
    version = ""
    year_from = ""
    year_to = ""
    power_from = ""
    power_to = ""
    powertype = "kw"
    num_pages = 20
    zipr = 50

    downloaded_listings_file = f'listings/listings_{make}_{model}.csv'
    output_file_preprocessed = f'listings/listings_{make}_{model}_preprocessed.csv'
    # Create the "listings" folder if it doesn't exist
    if not os.path.exists("listings"):
        os.makedirs("listings")

    scraper = AutoScout24Scraper(make, model, version, year_from, year_to, power_from, power_to, powertype, zip_list, zipr)
    scraper.scrape(num_pages, True)
    scraper.save_to_csv(downloaded_listings_file)
    scraper.quit_browser()


if __name__ == "__main__":
    main(scrape=True)
