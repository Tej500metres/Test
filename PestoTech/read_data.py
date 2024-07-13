import csv


def read_test_data(file_path):
    data = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


test_data = read_test_data("test_data.csv")
print(test_data)
