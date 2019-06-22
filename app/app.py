import os
import re
from flask import Flask, render_template, request

# Initialize the flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        print(password)
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)