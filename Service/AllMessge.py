from mongo import AllMessageMongo


def AllMensaje():
    result = []
    for x in AllMessageMongo.realizoQuery():
        x['_id'] = str(x['_id'])
        result.append(x)
    return result
