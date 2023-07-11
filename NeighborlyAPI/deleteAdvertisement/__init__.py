import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://neighborlyapp-db-account:lgr0OmgmQEMg2XFHOcZeO0C5ytHbWkWWif3j9xeJikVPGNghGcQUIzOZBOdTy81DjROpYmfL99Q6ACDbrnsYzg==@neighborlyapp-db-account.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlyapp-db-account@"
            client = pymongo.MongoClient(url)
            database = client["neighborlyapp_db"]
            collection = database["advertisements"]

            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
