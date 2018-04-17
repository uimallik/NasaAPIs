import requests
import json
import config
from pymongo import MongoClient
# Configuring the NASA API
response = requests.get(config.API)

# Response to JSON
data = response.json()
allcams = []

# Connecting to mongodb
client = MongoClient(config.url)
db = client[config.dbname]



# Method to GET the cameras in mars rover
def rov(mars_rover):
    for key, value in data.items():
        for length in range(len(value)):
            select_rover = value[length]
            for d in select_rover.items():
                if (d[0]=="rover"):
                    r = json.dumps(d[1])
                    resp = json.loads(r)


                    # Rover name
                    rov_name = str(resp['name'])
                    if (rov_name==mars_rover):
                        # Rover cameras
                        rov_cameras = (resp['cameras'])
                        listOfDicts = rov_cameras
                        for cameras in listOfDicts:

                            listOfCameras = str(cameras['name'])
                            allcams.append(listOfCameras)
                    else:
                        print("Choose Existing Rover name")
                    allcamsres = list(set(allcams))


    result = {"rover":rov_name,"listOfCameras":allcamsres}
    posts = db.result
    posts.insert_one(result)
    return result



# calling the method passing the parameter as rover name
result = rov("Curiosity")
print(result)















