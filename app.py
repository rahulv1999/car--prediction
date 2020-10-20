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
        yrs = request.form['yrs']
        currentprice = request.form['currentprice']
        km = request.form['km']
        fueltype = request.form['fueltype']
        sellertype = request.form['sellertype']
        transmission = request.form['transmission']
        owners = request.form['owners']
        
        if fueltype == 'petrol':
            petrol =1
            deisel =1
        elif fueltype =='diesel':
            petrol =0
            deisel =1
        else:
            petrol =0
            deisel =0
            
        if sellertype =='individual':
            individual = 1
        else:
            individual = 0
            
        if transmission == 'manual':
            manual = 1
        else:
            manual = 0
            
            
        data = np.array([currentprice, km, owners, yrs, deisel, petrol, individual, manual])
        data = data.reshape(1,-1)
        output =  (model.predict(data))
        k = round(output[0],2)
        f = open('templates/test.txt','w')
        f.write("\n thank god it worked")
        f.close()
        f = open('templates/test.txt','r')
        return render_template('index2.html', output = "{}".format(f.read()))
     
 
    
if __name__ == "__main__":
    app.run(debug=True)
