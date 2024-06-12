import csv

fileds = []
rows = []

filename = 'nasze_dane_2.csv'

with open(filename, 'r') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter, dialect.quotechar)  # ; "
    f.seek(0)  # odczyt na początek pliku
    # csvreader = csv.reader(f, delimiter=";")
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x0000018D2C0C58A0>

    fileds = next(csvreader)
    for row in csvreader:
        # print(row)
        rows.append(row)
print(fileds)  # ['name', 'branch', 'year', 'cgpa']
print(rows)
# [['radek', 'coe', '3', '9.1'],
# ['tomek', 'cot', '1', '9'],
# ['zenek', 'cos', '2', '9.7'],
# ['Marek', 'cow', '2', '9.19']]
#
# ['name;branch;year;cgpa']
# ['radek;coe;3;9.1']
# ['tomek;cot;1;9']
# ['zenek;cos;2;9.7']
# ['Marek;cow;2;9.19']
# ['name', 'branch', 'year', 'cgpa']
# ['radek', 'coe', '3', '9.1']
# ['tomek', 'cot', '1', '9']
# ['zenek', 'cos', '2', '9.7']
# ['Marek', 'cow', '2', '9.19']
