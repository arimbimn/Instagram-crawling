import pymongo
import json

# ubah nama json file yang akan di upload ke mongoDB menjadi 'insert.json'
# jalankan mongo lewat cmd
# jalankan mongod lewat cmd

namafile = 'insert.json'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ig_database"] #nama database
mycol = mydb["accounts"] #nama tabel

mylist = []

with open(namafile) as json_file:
    data = json.load(json_file)
    for p in data:
        mylist.append(p)


x = mycol.insert_many(mylist)

print(x.inserted_ids)
