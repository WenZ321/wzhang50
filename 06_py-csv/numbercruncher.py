#Wen Zhang
#China Rats plus One
#Soft Dev
#<Processing a csv file(python dictionaries) and using weight percentages to select a random job>
#2024-09-19
#Time spent: ~30 minutes

import random
import csv

occupation_list = []
percentages = []

with open('occupations.csv', newline ='') as csvfile:
    file = csv.DictReader(csvfile)
    for row in file:
        occupation_list.append(row['Job Class'])
        percentages.append((float)(row['Percentage']))

occupation_list = occupation_list[1:-1]
percentages = percentages[1:-1]

def select_occupation(occupation_list, percentages):
    selected = random.choices(occupation_list, weights=percentages, k=1)
    return selected[0]

for i in range(100):
        print(select_occupation(occupation_list, percentages))