import csv
import os

def get_dict(file):

    d = {}

    # get the path to the current file
    path = os.path.dirname(os.path.abspath(__file__))
    file_full_path = os.path.join(path, file)

    # get the file handler
    inFile = open(file_full_path)
    csvFile = csv.reader(inFile)

    # skip the header
    headers = next(inFile)

    # read the rest of the lines from the file handler
    for row in csvFile:

        if len(row) == 4:
            month = row[0]
            data_1 = int(row[1])
            data_2 = int(row[2])
            data_3 = int(row[3])

            year_d = {}
            year_d[headers[0]] = data_1
            year_d[headers[2]] = data_2
            year_d[headers[3]] = data_3
            d[month] = year_d

    inFile.close()
    return d

def get_max_month(travel_d, year):
    d = {}
    for month in travel_d:
        month_d = travel_d[month]
        d[month] = month_d[year]
    tup_list = sorted(d.items(), key = lambda t: t[0], reverse = True)
    return tup_list[0]

travel_d = get_dict("airtravel.csv")
print(travel_d)
month, amount = get_max_month(travel_d, "1958")
print(month, amount)