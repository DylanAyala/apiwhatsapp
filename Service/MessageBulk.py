from mongo import MessageBulkMongo


def messageBulk(data):
    MessageBulkMongo.insert(data)
