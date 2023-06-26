import requests
import pandas as pd
import os
from urllib.parse import urljoin


def download_and_convert(language):
    base_url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/"

    # Define URL for the 50k words file
    file_50k = f"{language}/{language}_50k.txt"
    url_50k = urljoin(base_url, file_50k)

    # Define URL for the full words file
    file_full = f"{language}/{language}_full.txt"
    url_full = urljoin(base_url, file_full)

    response = requests.get(url_50k)
    if response.status_code == 200:
        data = response.text
        csv_filename = f"./backend/data/lists/{language}_50k.csv"
    else:
        response = requests.get(url_full)
        if response.status_code == 200:
            data = response.text
            csv_filename = f"./backend/data/lists/{language}_full.csv"
        else:
            print("No suitable file found for the provided language.")
            return

    # Check if the file already exists
    if os.path.exists(csv_filename):
        print(f"File already exists: {csv_filename}")
        return

    # Convert txt data to csv and save
    txt_to_csv(data, csv_filename)


def txt_to_csv(data, csv_filename):
    lines = data.split("\n")

    data = []
    for line in lines:
        if line:
            data.append(line.split())

    df = pd.DataFrame(data, columns=["Word", "Frequency"])
    df.to_csv(csv_filename, index=False)
    print(f"File converted to CSV: {csv_filename}")


# Load supported languages
languages = []
with open("backend/data/lists/supported_languages.txt", "r") as file:
    languages = [line.strip() for line in file]

# Download and convert data for each language
for language in languages:
    download_and_convert(language)
