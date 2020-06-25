import json
import os

import boto3
import pymongo
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(dotenv_path=".env")

s3 = boto3.client("s3")

BUCKET = "puppies-ddh"
KEY = "puppies.json"

mongo_client = pymongo.MongoClient(os.environ["ATLAS_URI"])


TWILIO_SID = (os.environ["TWILIO_SID"])
TWILIO_TOKEN = (os.environ["TWILIO_TOKEN"])


twilio_client = Client(TWILIO_SID, TWILIO_TOKEN)


def handler(event, context):
    puppy_list = getJson()
    db = mongo_client["puppies"]
    collection = db["puppies"]

    for pup in puppy_list:
        if (not(collection.find_one({
            "name": pup["name"],
            "breed": pup["breed"]
        }))):
            collection.insert_one(pup).inserted_id
            if (pup["age"] == "Baby"):
                print(f"They added a baby! {pup['name']}")
                twilio_client.messages \
                    .create(
                        body=f"They added a baby! {pup['name']}",
                        from_=os.environ["FROM_PHONE"],
                        to=os.environ["TO_PHONE"]
                    )
        else:
            print(f"This pup is already in the Db: {pup['name']}")


def getJson():
    obj = s3.get_object(Bucket=BUCKET, Key=KEY)
    data = json.load(obj["Body"])
    return data
