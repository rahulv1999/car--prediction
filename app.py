import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('car_prediction.pkl','rb'))

@app.route('/')
def home():
    return render_template('index2.html')
    

@app.route('/predict', methods = ['POST'])
def predict():
    
    #to render result in html GUI
    
    if request.method == 'POST':
        f = open('templates/test.txt','a')
        f.write("\n thank god it worked")
        f.close()
        f = open('templates/test.txt','r')
        return render_template('index2.html', output = "{}".format(f.read()))
     
 
    
if __name__ == "__main__":
    app.run(debug=True)
