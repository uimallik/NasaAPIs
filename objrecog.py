from watson_developer_cloud import VisualRecognitionV3
import json
import pyttsx


# Image capture from webcam
import cv2

# Camera 0 is the integrated web cam on my netbook
camera_port = 0
#camera_port = 'https://192.168.1.251:8080'


#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30

# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)

# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im

# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
 temp = get_image()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = get_image()
file = "/home/default/mkimage.png"
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)

# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)












visual_recognition = VisualRecognitionV3('2016-05-20', api_key='xxxxxxxxxxxxxxxxxxxxxxxxxxx')

parameters = json.dumps({'threshold': 0.1, 'classifier_ids': ['default']})
image_file = open('mkimage.png','r')
url_result = visual_recognition.classify(images_file=image_file,parameters=parameters)
result = json.dumps(url_result, indent=2)

resp = json.loads(result)
for key,value in resp.items():
    xs = value[0]
    #print xs
    for k,v in xs.items():
        if(k=="classifiers"):
           xy = v[0]
           for ke,ve in xy.items():
               if(ke=="classes"):
                 xu = ve[0]
                 for keys,val in xu.items():
                     if(keys=="class"):
                        print val
                        val =  "It is a "+val
                        # Text to speech
                        engine = pyttsx.init()
                        engine.setProperty('rate', 120)
                        engine.say(val)
                        engine.runAndWait()
                 break
           break
    break
