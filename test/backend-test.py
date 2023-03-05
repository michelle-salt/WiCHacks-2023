from flask import Flask, request, jsonify
import datetime
import json
import random
import requests

class Data:
    store = None
    price = [] # 1st item is the one from the API, rest are "historical"
    image = None 
    date = [] # 1st item is the one from the API, rest are one week apart

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__, 
    #     sort_keys=True, indent=4)

class DataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Data):
            return {
                'store': obj.store,
                'price': obj.price,
                'image': obj.image,
                'date': [date.isoformat() for date in obj.date]
            }
        else:
            return super().default(obj)

def getCookedData(postalCode, foodItem):
    # in theory the following two things would be passed through in the API
    # postalCode = "L4J5K2"
    # foodItem = "detergent"

    url = "https://backflipp.wishabi.com/flipp/items/search?locale=en-ca&postal_code=" + postalCode + "&q=" + foodItem

    rawData = requests.get(url).json()

    # parse the json data and put it in the class
    cookedData = Data()
    cookedData.store = rawData['items'][0]['merchant_name']
    cookedData.price.append(rawData['items'][0]['current_price'])
    cookedData.image = rawData['items'][0]['clean_image_url']
    tempdate = datetime.datetime.fromisoformat(rawData['items'][0]['valid_to'])
    cookedData.date.append(tempdate) 
    storeName = rawData['items'][0]['valid_to']

    # define range for generating new numbers for price range
    min_val = cookedData.price[0] - 3
    max_val = cookedData.price[0] + 3

    # generate 9 random floats and add them to the price array
    for i in range(9):
        new_int = abs(random.uniform(min_val, max_val))
        new_int = format(new_int, '.2f')
        cookedData.price.append(new_int)

    # get the rest of the dates one week apart from the current date
    for i in range(1, 10):
        new_date = cookedData.date[0] - datetime.timedelta(weeks=i)
        cookedData.date.append(new_date)

    # print out the data
    for attribute in dir(cookedData):
        if not attribute.startswith("__"):  # exclude built-in attributes
            print(f"{attribute}: {getattr(cookedData, attribute)}")
    print("\n")

    json_str = json.dumps(cookedData, cls=DataEncoder)

    return json_str

app = Flask(__name__)

@app.route("/api", methods = ['GET'])
def returnCookedData():
    postalCode = str(request.args['postalcode'])
    foodItem = str(request.args['item'])
    res = {}
    res['output'] = getCookedData(postalCode, foodItem)
    return res

if __name__ =="__main__":
    app.run()