print("csv file")

import csv

with open('profiles1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name"]

    writer.writerow(field)
    writer.writerow(["Oladele Damilola"])
    writer.writerow(["Alina Hricko"])
    writer.writerow(["Isabel Walter"])