import re
import json
from bs4 import BeautifulSoup

# Sample HTML document
input_dir = r"html_files\VIBORG LANDSTINGS DOMBØGER 1665-1666.html"

data = {}
cnregex = re.compile(r'^\(\d+\)')
yregex = re.compile(r'.*\b\d{4}\b.*')
cregex = re.compile(r'^\*\*')

with open(input_dir, encoding="windows-1252") as fp:  # Specify encoding as windows-1252
    soup = BeautifulSoup(fp, 'html.parser')
    tablecells = soup.find_all('td')

    current_year = ''  # Initialize current year to empty string
    pending_casenumber = ''  # Initialize pending casenumber to empty string

    for p in tablecells:
        paragraphs = p.find_all('p')

        for paragraph in paragraphs:
            text = paragraph.get_text().strip()
            print("Current Text:", text)

            if yregex.match(text):
                # Update current year when a year is found
                current_year = text
                if current_year not in data:
                    data[current_year] = {}

                # Check if there are pending casenumbers
                if pending_casenumber:
                    data.setdefault(current_year, {}).setdefault(pending_casenumber, set())  # Use a set to store case descriptions
                    pending_casenumber = ''  # Reset pending casenumber

                print("Current Year:", current_year)

            elif cnregex.match(text):
                # If casenumber is encountered before year, store it as pending
                pending_casenumber = text
                print("Encountered casenumber before year, stored as pending:", pending_casenumber)

            elif cregex.match(text):
                # Store the case description
                if current_year:
                    data.setdefault(current_year, {}).setdefault(pending_casenumber, set()).add(text)  # Add description to set
                else:
                    print("Warning: Case description found without year:", text)

            else:
                print("Warning: Unhandled paragraph:", text)

    print(data)

# Convert sets to lists for JSON serialization
for year, cases in data.items():
    for case, descriptions in cases.items():
        data[year][case] = list(descriptions)

# Define the file path where you want to save the JSON file
output_file_path = "case_data 1665-1666.json"

# Write the data dictionary to the JSON file with UTF-8 encoding
with open(output_file_path, 'w', encoding="utf-8") as json_file:  # Specify encoding as UTF-8
    json.dump(data, json_file, indent=4, ensure_ascii=False)  # Ensure_ascii to False for proper encoding of non-ASCII characters

print("Data has been successfully exported to:", output_file_path)
