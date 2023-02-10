
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.catalogue
students = db.books
book = {
    "title": "A Light in the Attic",
}
document_id = db.books.insert_one(book).inserted_id
print(document_id)
client.close()
