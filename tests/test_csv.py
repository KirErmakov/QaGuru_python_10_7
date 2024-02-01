import csv
import os

def test_csv(create_zip):
    csv_path = os.path.join(create_zip, 'users.csv')
    with open(csv_path) as file:
        reader = csv.reader(file)
        for row in reader:
            assert isinstance(row, list)
            print(row)
