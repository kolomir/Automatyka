import csv
file = open("zestawienie.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

for linia in rows:
    print(linia)