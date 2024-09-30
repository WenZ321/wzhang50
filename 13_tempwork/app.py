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

with open('occupations.csv', newline ='') as csvfile:
    file = csv.DictReader(csvfile)
    occupation_dict = file

occupation_dict = occupation_dict[1:-1]

def select_occupation(occupation_list, percentages):
    return random.choices(occupation_list, weights=percentages, k=1)
     
    # -------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/wdywtbwygp")
def page():
    occupation = select_occupation(occupation_list, percentages)
    
    
    
    return html
    
    
if __name__ == "__main__":      
    app.debug = True            
    app.run()
