import csv
import json
from collections import defaultdict

# Make as many dictionaries needed for each period of schedule
period = {} 
megadictionary = defaultdict(list)

csv_file_input = ""
json_output = ""

# Repeat the same process for each period of schedule
with open(csv_file_input, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        periods = row['Periods']
        # Format: day_of_rotation(period)
        # Change the period number for each copy
        if periods[0:4] == '1(1)':
            # Special case
            for key, value in row.items():
                row[key] = value.replace('Example text value in schedule', 'Corresponding room reference number')
            period['Student ID'] = row['Student ID']
            period['Day 1 Schedules'] = row['Classroom']

with open(json_output, 'w') as file:
    for d in period:
        for key, value in d.items():
            megadictionary[key].append(value)
            json.dump(megadictionary, file, sort_keys=False, indent=4)