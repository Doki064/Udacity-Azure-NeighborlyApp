import azure.functions as func
import pymongo


def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://neighborlyapp-db-account:lgr0OmgmQEMg2XFHOcZeO0C5ytHbWkWWif3j9xeJikVPGNghGcQUIzOZBOdTy81DjROpYmfL99Q6ACDbrnsYzg==@neighborlyapp-db-account.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlyapp-db-account@"
            client = pymongo.MongoClient(url)
            database = client["test"]
            collection = database["advertisements"]

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
