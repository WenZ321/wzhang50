import random
import csv

occupation_list = []

with open('occupations.csv', newline ='') as csvfile:
    file = csv.DictReader(csvfile)
    for row in file:
        occupation_list.append(row)

print(occupation_list)