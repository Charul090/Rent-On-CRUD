import jwt
from instance.config import SECRET_KEY as key
import datetime


def check_auth_token(token):

    decoded_data = jwt.decode(token, key)

    if datetime.datetime.strptime(decoded_data["expire_at"],
                                  "%Y-%m-%d %H:%M:%S.%f") \
    < datetime.datetime.utcnow():
        return False, {}
    else:
        return True, {"email": decoded_data["email"],
                      "type": decoded_data["type"]}
