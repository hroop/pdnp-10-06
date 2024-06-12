import csv

# pliki csv

# pliki w których dane oddzielone są znakiem podziału (, tab;)
# Radek, Zenek, Marek

filname = 'records.csv'
row = ['radek', 'coe', 3, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']

dictionary = dict(zip(fields, row))
print(dictionary)  # {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.1'}

dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.1'},
    {'name': 'tomek', 'branch': 'cot', 'year': 1, 'cgpa': '9'},
    {'name': 'zenek', 'branch': 'cos', 'year': 2, 'cgpa': '9.7'},
    {'name': 'Marek', 'branch': 'cow', 'year': 2, 'cgpa': '9.19'},

]
with open(filname, 'w', newline='') as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filname = 'nasze_dane_2.csv'
with open(filname, 'w', newline='') as fh:
    csvwriter = csv.DictWriter(fh, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    # zapisanie danych z pojedynczego słownika
    # csvwriter.writerow(dictionary)
    csvwriter.writerows(dict_list)
