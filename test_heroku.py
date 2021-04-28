import requests
import json

#load testdata
with open('datatest.json', 'r') as f:
    testdata = json.load(f)

r = requests.post('http://127.0.0.1:5000/predict', json = {'newdata': testdata})

data = r.json()

for pred in data:
  print(f'Based on the data provided, this cell phone is {"{:.0%}".format(pred[1])} likely to be running malware')
