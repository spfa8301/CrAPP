import requests
import json

with open('testdata.json','r') as f:
    testdata = json.load(f)

r=requests.post('http://127.0.0.1:5000/predict', json={'newdata': testdata})
data = r.json()
prediction = data['prediction']
print(prediction)
#print(f'probability is {prediction}')
