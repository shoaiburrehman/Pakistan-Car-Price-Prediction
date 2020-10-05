#import requests

#url = 'http://localhost:5000/predict_api'
#data = {
#       "Brand": "Suzuki",
#       "Condition": "Used",
#       "Fuel": "CNG",
#       "KMs Driven": 73000,
#       "Model": "Liana",
#       "Registered City": "Karachi",
#       "Transaction Type": "Cash",
#       "Year": 2006
#        }
#data = predic_index(data["input"])

#r = requests.post(url, json=data)

#print(r.json())

import requests 
from data_input import data_in
from model import data_all

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}

#data = {"input": data_in}
data = data_all(1)
#print(data)


r = requests.get(URL, json=data) 


r.json()