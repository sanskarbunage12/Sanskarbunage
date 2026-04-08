import csv
import json

data = []

# Read CSV
with open("output.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        data.append(row)

# Convert to JSON
json_data = json.dumps(data, indent=4)

print(json_data)