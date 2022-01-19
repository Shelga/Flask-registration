import shortuuid


def get_hash(password): 

    hashPassword = shortuuid.uuid(password)[:20]

    return hashPassword