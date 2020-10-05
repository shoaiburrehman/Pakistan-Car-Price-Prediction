import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import json
from model import predic_index, price_estimate, predict_price
from data_input import data_in
from numpy import *
#file_name = "models/dtree_car_price_model.pickle"
#model = pickle.load(open(file_name, 'rb'))
#print(model)

def load_models():
    file_name = "models/dtree_car_price_model.pickle"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        #print(data)
        #model = data['model']
        #print(model)
    return data

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/predict', methods=['GET'])
# def predict():
#     # stub input features
#     request_json = request.get_json()
#     x = request_json['input']
#     #print(x)
#     x_in = np.array(x).reshape(1,-1)
#     # load model
#     model = load_models()
#     prediction = np.exp(model.predict(x_in)[0])
#     output = round(prediction, 0)
#     print("Output: ", output)
#     response = json.dumps({'response': output})
#     return render_template('index.html', prediction_text='Car Price should be ${}'.format(output))

# if __name__ == '__main__':
#     app.run(debug=True)
#@app.route('/')
#def home():
#    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    ''' 
    features = [x for x in request.form.values()]
    print("features value: ", features)
    #int_features = int(x)
    #final_features = int(np.array(int_features))
    print("int_features[0]: ", features[0])
    #x_val = int_features[0]
    x_num = [features[3], features[7]]
    x_cat = [str(features[0]), str(features[1]), str(features[2]), str(features[4]), str(features[5]), str(features[6])]
    print('Numerical Value: ', x_num)
    print('Categorical Value: ', x_cat)

    model = load_models()
    prediction = np.exp(predict_price(x_cat, x_num, model))
    output = round(prediction, 0)
    print("Output predict: ", output)
    return render_template('index.html', prediction_text='Car Predicted Price is Rs. {}'.format(output))


@app.route('/predict_api',methods=['GET'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    request_json = request.get_json()
    #x = request_json['Brand', 'Condition', 'Fuel', 'KMs Driven', 'Model', 'Registered City', 'Transaction Type', 'Year']
    #print(x)
    print('request json: ', request_json['KMs Driven'])
    x_in = np.array(list(request_json.values())).reshape(1,-1)
    print('x input: ', x_in[0])
    x_val = x_in[0]
    #print('x Value: ', x_val[3])    
    # numerical_val = []
    # numerical_val = str(x_val[3])
    #x_num = np.array(list(numerical_val)))
    #x_num = [numerical_val]
    # numerical_val2 = str(x_val[7])
    x_num = [x_val[3], x_val[7]]
    x_cat = [str(x_val[0]), str(x_val[1]), str(x_val[2]), str(x_val[4]), str(x_val[5]), str(x_val[6])]
    print('Numerical Value: ', x_num)
    print('Categorical Value: ', x_cat)

    # load model

    model = load_models()
    prediction = predict_price(x_cat, x_num, model)
    print('prediction: ', prediction)
    output = round(np.exp(prediction), 0)
    print("Output response: ", output)
    response = json.dumps({'response': output})
    return response, 200


if __name__ == "__main__":
    app.run(debug=True)