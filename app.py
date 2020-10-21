import os
from werkzeug.utils import secure_filename
from flask import Flask,flash,request,redirect,send_file,render_template,send_from_directory



#app = Flask(__name__)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/downloads/')
def downloads():
    #return send_file('templates\\text.txt',attachment_filename='text.txt')
    return send_from_directory(directory='templates',filename='result_mate.csv',as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
