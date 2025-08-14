import csv
with open('/Users/mehulgupta/Documents/Python/bank_records.csv','r') as f:
    reader = csv.reader(f)
    for x in reader:
        print(x)