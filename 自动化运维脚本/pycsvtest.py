import csv
with open('C:\Users\Administrator\Desktop\ip.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)