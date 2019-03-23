from pymongo import MongoClient

conection = MongoClient('localhost', 27017)

dataBase = conection['testdb']

collection = dataBase['Mensajes']


def realizoQuery():
    result = collection.find()
    return result
