import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://neighborlyapp-db-account:lgr0OmgmQEMg2XFHOcZeO0C5ytHbWkWWif3j9xeJikVPGNghGcQUIzOZBOdTy81DjROpYmfL99Q6ACDbrnsYzg==@neighborlyapp-db-account.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlyapp-db-account@"
        client = pymongo.MongoClient(url)
        database = client["neighborlyapp_db"]
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)
