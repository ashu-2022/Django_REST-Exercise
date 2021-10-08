# This application is write in any programming language
# it deals with API
# for testing purpose we build using python 
# it may be any java android, node web application

import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'


def get_data(id = None):
    data = {}
    if id is not None :
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    r =requests.get(url = URL,data = json_data, headers=headers)
    response_data = r.json()
    print(response_data)

get_data()

def post_data():
    data = {
        'name' : 'Anshu',
        'roll' : 38,
        'city' : 'Sahibabad'
    }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)
    r =requests.post(url = URL,data = json_data, headers=headers)
    response_data = r.json()
    print(response_data)
    
# get_data()
# post_data()
# get_data()


def update_data():
    # provide id must to update
    data = {
        'id' : 11 ,
        'city' : 'Khora Colony'
    }
    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    r =requests.patch(url = URL,data = json_data, headers=headers)
    response_data = r.json()
    print(response_data)

# get_data()
update_data()
# get_data()   

def delete_data():
    data = {'id' : 8}
    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    r =requests.delete(url = URL,data = json_data, headers=headers)
    response_data = r.json()
    print(response_data)

# get_data()
# delete_data()
# get_data()