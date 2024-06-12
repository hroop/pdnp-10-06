import pandas

# pip install pandas

data = pandas.read_csv('nasze_dane_2.csv', delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  radek    coe     3  9.10
# 1  tomek    cot     1  9.00
# 2  zenek    cos     2  9.70
# 3  Marek    cow     2  9.19
print(data.columns)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['radek' 'coe' 3 9.1]
#  ['tomek' 'cot' 1 9.0]
#  ['zenek' 'cos' 2 9.7]
#  ['Marek' 'cow' 2 9.19]]
print(data.items)
# <bound method DataFrame.items of     name branch  year  cgpa
# 0  radek    coe     3  9.10
# 1  tomek    cot     1  9.00
# 2  zenek    cos     2  9.70
# 3  Marek    cow     2  9.19>
