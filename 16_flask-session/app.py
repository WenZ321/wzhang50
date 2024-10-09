# Clyde 'Thluffy' Sinclair
# SoftDev
# October 2024

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


@app.route("/") 
def disp_loginpage():

    return render_template( 'login.html' )


@app.route("/auth")
def responsePage():
    username = request.args['username']
    responseSite = render_template( 'response.html', username) #response to a form submission
    responseSite.set_cookie("userID", username)
    return responseSite

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

