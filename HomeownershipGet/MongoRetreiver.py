import os
import stat
import subprocess
import pymongo
import csv
import json
import bsonjs
from bson.raw_bson import RawBSONDocument

client = pymongo.MongoClient("mongodb+srv://khary:Mi$%40Toni1524@cluster0-zkptn.azure.mongodb.net/GiniInternationalDB")
db = client.get_database()

# subprocess.check_output(["kaggle", "datasets", "download", "-d", "census/homeownership-rate-time-series-collection"])
# subprocess.check_output(["unzip", "homeownership-rate-time-series-collection.zip", "-d", "HomeownershipRateTime"])
#
json_path = "C:\\Users\Khary\VSCodeProjects\CensusDataAPI\FlaskRESTServer\\temp_json_holder.json"
#
# directory_in_str = "/home/kfiler/PycharmProjects/CensusDataGetter/HomeownershipGet/HomeownershipRateTime"
# directory = os.fsencode(directory_in_str)
#
# for entry in os.scandir(directory):
#     filename = os.fsdecode(entry.path)  # entry.path is returned in bytes. Have to decode to get a string
#     if filename.endswith(".csv"):
#         os.chmod(entry.path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
#         # with block automatically closes the file when the block ends
#         with open(entry.path, "rU") as temp_csv:
#             reader = csv.DictReader(temp_csv, fieldnames=("realtime_start", "realtime_end", "date,value"))
#             out = json.dumps([row for row in reader])
#             with open(json_path, "w") as temp_json:
#                 temp_json.write(out)
#                 bson_bytes = bsonjs.loads(out)
#                 post = db.HomeownershipRateTimeSeriesCollection
#                 post_id = post.insert_one(RawBSONDocument(bson_bytes)).inserted_id
#
# subprocess.check_output(["rm", "homeownership-rate-time-series-collection.zip"])
# subprocess.check_output(["rm", "-rf", "HomeownershipRateTime/"])

csv_path = "C:\\Users\Khary\VSCodeProjects\CensusDataAPI\FlaskRESTServer\GiniInternationalData.csv"

with open(csv_path, "r") as temp_csv:
    reader = csv.DictReader(temp_csv, delimiter=",")
    out = json.dumps([row for row in reader])
    with open(json_path, "w") as temp_json:
        temp_json.write(out)
        bson_bytes = bsonjs.loads(out)
        post = db.GiniInternational
        post_id = post.insert_one(RawBSONDocument(bson_bytes)).inserted_id

