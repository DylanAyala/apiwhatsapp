from pymongo import MongoClient

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['MensajesBulk']


def insert(data):
    collection.insert_one(data)
