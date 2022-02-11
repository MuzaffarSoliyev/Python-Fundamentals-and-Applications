import csv
import re

crimes = {}

with open('Crimes.csv') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        year = re.findall(r'[0-9]{4}', row[2])
        if len(year) > 0:
            if year[0] == '2015':
                if row[5] in crimes.keys():
                    crimes[row[5]] += 1
                else:
                    crimes[row[5]] = 1

max_val = 0
max_key = 0
for key, val in crimes.items():
    if val > max_val:
        max_val = val
        max_key = key

print(max_key, max_val)
