import time
import datetime
import pymongo
import RPi.GPIO as GPIO
import dht11
from bson.objectid import ObjectId

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)
client=pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.rv38o.mongodb.net/temp-humidity-datas?retryWrites=true&w=majority")
db=client["temp-humidity-datas"]
col=db["datas"]
try:
        result = instance.read()
        if result.is_valid():
                print("Last valid input: " + str(datetime.datetime.now()))
                print("Temperature: %-3.1f C" % result.temperature)
                print("Humidity: %-3.1f %%" % result.humidity)
                time.sleep(5)
                time_now=datetime.datetime.now()
                datas={"measurement time":time_now.ctime(),"temperature": str(result.temperature)+" C","humidity":"%"+str(result.humidity)}
                col.insert_one(datas)
                
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()



