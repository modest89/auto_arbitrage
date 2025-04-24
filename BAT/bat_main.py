import subprocess
import datetime

# List of scripts to run
scripts = [
    r"C:\Users\Modest\OneDrive\_With Modest (ONLY)\Various\Power Bi\BAT\_unique\bringyourtrailer_alfa_giulia.py",
    r"C:\Users\Modest\OneDrive\_With Modest (ONLY)\Various\Power Bi\BAT\_unique\bringyourtrailer_alfa_giulietta.py",
    r"C:\Users\Modest\OneDrive\_With Modest (ONLY)\Various\Power Bi\BAT\_unique\bringyourtrailer_audi_avant.py",
    r"C:\Users\Modest\OneDrive\_With Modest (ONLY)\Various\Power Bi\BAT\_unique\bringyourtrailer_bmw_128.py",
    r"C:\Users\Modest\OneDrive\_With Modest (ONLY)\Various\Power Bi\BAT\_unique\bringyourtrailer_bmw_135.py",
    r"C:\Users\Modest\OneDrive\_With Modest (ONLY)\Various\Power Bi\BAT\_unique\bringyourtrailer_bmw_b3.py",
    r"C:\Users\Modest\OneDrive\_With Modest (ONLY)\Various\Power Bi\BAT\_unique\bringyourtrailer_ford_rs.py",
    r"C:\Users\Modest\OneDrive\_With Modest (ONLY)\Various\Power Bi\BAT\_unique\bringyourtrailer_ford_st.py",
    r"C:\Users\Modest\OneDrive\_With Modest (ONLY)\Various\Power Bi\BAT\_unique\bringyourtrailer_golf_gti.py",
    r"C:\Users\Modest\OneDrive\_With Modest (ONLY)\Various\Power Bi\BAT\_unique\bringyourtrailer_vw_scirocco.py"
]

# Function to run a script
def run_script(script_path):
    subprocess.run(["python", script_path], check=True)

# Get the current day of the week
current_day = datetime.datetime.now().weekday()

# Check if it's Friday (weekday number 4, since Monday is 0 and Sunday is 6)
if current_day == 5:
    # Run each script one after another
    for script in scripts:
        run_script(script)
else:
    print("It's not Friday. Exiting script without running anything.")
