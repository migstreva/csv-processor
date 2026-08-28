import csv

def read_sales(file_path):
    sales = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            sales.append(row)

    return sales