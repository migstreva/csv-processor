import csv

def read_sales():
    sales = []
    with open("../data/sales.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            sales.append(row)

    return sales