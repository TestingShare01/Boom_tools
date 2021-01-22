import uuid
from logzero import logger
import hashlib
def set_token():
    uid = str(uuid.uuid1())
    logger.info(str(uid))
    hash = hashlib.md5(uid.encode(encoding="UTF-8")).hexdigest()
    return hash
