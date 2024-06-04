import re
import json
from pathlib import Path

# Define input and output file paths
input_file_path = r'json_files\case_data 1569-1591.json'
output_file_path = r'filtered_json\filtered_data 1569-1591.json'

# List of keywords
keyword_list = [
    "død", "bane", "manddød", "slog", "ihjel", "ihjelslog", "dræbt", "livs",
    "fredløse", "sagesløse", "lig", "dræbte", "slagsmål", "sårmål", "myrdet",
    "mord", "dødfundet", "banesår", "fredløs", "dødelige", "manddrab", "fredløsmål",
    "dødt", "banemand", "æresløs", "såret", "overfald", "trussel", "dødssår",
    "dødes", "manddræberen", "sønderslået", "sønderrevet", "sønderlade",
    "ihjelstukket", "ihjelskød", "ihjelskudt", "manddræberens", "livsfare",
    "ihjelstak", "ihjelslaget", "dødfunden", "manddræber", "forgive", "dræberens",
    "dræbe", "banemænd", "aflives", "afhuggen", "afhug", "udød", "sønderslog",
    "nedhugge", "meddræber", "manddræbers", "manddrabs", "henrettelse", "henrette",
    "fredløst", "dødsskade", "dødskudt", "dødsår", "dødeligt", "dræbtes", "dræbes",
    "dræber", "ihjelslået", "nødværge", "omkommet", "sandemænd"
]

# Compile regex pattern
keyregex = re.compile(rf'\b(?:{"|".join(keyword_list)})\b', re.I)

# Load JSON data with UTF-8 encoding
with open(input_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

filtered_data = {}

# Iterate through each date
for date, cases in data.items():
    filtered_cases = {}

    # Iterate through each case
    for case_number, case_descriptions in cases.items():
        matched_descriptions = []

        # Iterate through each description and check for matches
        for description in case_descriptions:
            matches = keyregex.findall(description)
            if matches:
                matched_descriptions.append(description)

        # If there are matched descriptions, add them to the filtered cases
        if matched_descriptions:
            filtered_cases[case_number] = matched_descriptions

    # If there are filtered cases for this date, add them to the filtered data
    if filtered_cases:
        filtered_data[date] = filtered_cases

# Write filtered data to a new JSON file with UTF-8 encoding
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, indent=4, ensure_ascii=False)

print("Filtered data has been written to:", output_file_path)
