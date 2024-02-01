import csv
import os

def test_csv(create_zip):
    csv_path = os.path.join(create_zip, 'users.csv')
    with open(csv_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
