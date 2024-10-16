# Wen Zhang, Yinwei Zhang, Jackie Zeng
# Made In China
# SoftDev
# K16 <Flask Forms, Cookies>
# 2024-10-8
# Time Spent : 2 Hours

from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
