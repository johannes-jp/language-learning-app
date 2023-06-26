# %%
import requests
from bs4 import BeautifulSoup
import csv
import os

word_list_sources = [
    {
        "name": "Wiktionary's Finnish 5000",
        "language": "fi",
        "url": "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Finnish_wordlist",
        "author": "wiktionary.com",
        "acknowledgements": "opensubtitles.com",
        "write_file": "finnish5000_opensubtitles.csv",
    },
    {
        "name": "Wiktionary's Icelandic 5000",
        "language": "is",
        "url": "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Icelandic_wordlist",
        "author": "wiktionary.com",
        "acknowledgements": "opensubtitles.com",
        "write_file": "icelandic5000_opensubtitles.csv",
    },
]


def get_list(source):
    response = requests.get(source["url"])
    soup = BeautifulSoup(response.text, "html.parser")

    entries = []
    for li in soup.find_all("li"):
        # Find the 'a' tag within the 'li'
        a_tag = li.find("a")
        try:
            # bind title and number in body if they exist
            title = a_tag.get("title")
            frequency = li.get_text().split(" ")[-1]
            # if the title has any baggage, split into 2 parts
            title_parts = title.split(" ", 1)
            word = title_parts[0]
            error_message = title_parts[1] if len(title_parts) > 1 else ""
        except Exception as e:
            print(e)
        if title and frequency.isdigit():
            print(a_tag)
            # Each entry will be a tuple containing the word, frequency, and error message
            entries.append((word, int(frequency), error_message))

    return entries


def write_csv(entries, write_file):
    # If file already exists, check if the number of lines in it are equal to the number of items in the 'entries' list
    if os.path.exists(write_file):
        with open(write_file, "r") as f:
            existing_lines = sum(1 for line in f)
            if existing_lines == len(entries):
                return

    # If file doesn't exist or the number of lines in it does not match with the number of entries, write the entries into the file
    with open(write_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Frequency", "Errors"])  # write header
        for entry in entries:
            writer.writerow(list(entry))  # write each entry as a row


for source in word_list_sources:
    write_csv(get_list(source), source["write_file"])
