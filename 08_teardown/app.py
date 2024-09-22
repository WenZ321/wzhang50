# your heading here

'''
DISCO:
<note any discoveries you made here... no matter how small!>
If I copy and paste the numbers of the servers into a browser, the website will have "NO Hablo Espanol"
When I changed what is in the return, the website also matches to what I changed

QCC:
0. In java, where we would create an object from a class. In this example, a Flask class.
1. This could be like going to the homepage
2. I think this will print to the console/terminal where the Flask server is running
3. I am not sure
4. I think it will appear on the website where the flask server is being runnmed
5. I have seen this in java, where we call a function of a class through an object of that class
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?