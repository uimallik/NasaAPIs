# NasaAPIs

## Extracting the camera list for particular mars rover

### Add configurations in the config.py
API = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=token"
url = "mongodb url"
dbname = "dbname"

### Dependencies
$pip install requests
$pip install pymongo

### Run app.py

Ref Source: https://api.nasa.gov/api.html#MarsPhotos
