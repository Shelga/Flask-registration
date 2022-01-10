import shortuuid


def get_hash(password): 

    hashPassword = shortuuid.uuid(password)[:8]

    return hashPassword