'''
Wen Zhang, Jackie Zeng, Danny Huang
Made in Africa
SoftDev
K13 -- creating template to make html table
2024-09-30
Time spent: 30 mins
'''

import random
import csv

occupation_dict = []
occupation_list = []
percentages = []

with open('data/occupations.csv', newline ='') as csvfile:
    file = csv.DictReader(csvfile)
    for row in file:
        occupation_list.append(row['Job Class'])
        percentages.append(float(row['Percentage']))
        occupation_dict.append([row['Job Class'], float(row['Percentage'])])
        

occupation_list = occupation_dict[0:-1]
occupation_list = occupation_list[1:-1]
percentages = percentages[1:-1]

def select_occupation(occupation_list, percentages):
    return random.choices(occupation_list, weights=percentages, k=1)
     
    # -------------------------------------------------------------



from flask import Flask, render_template
app = Flask(__name__)

@app.route("/wdywtbwygp")
def page():
    occupation = select_occupation(occupation_list, percentages)
    return render_template('tablified.html', title = "Job Table", Job = occupation[0], Occ = "Jobs", collection = occupation_dict)
    
    
if __name__ == "__main__":      
    app.debug = True            
    app.run()
