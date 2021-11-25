from jose import JWTError, jwt
from datetime import datetime, timedelta


SECRET_KEY = ""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data:dict):
    """[Generate access token with HS256]

    Args:
        data (dict): [return secret token]

    Returns:
        [dict]: [return a dictionary of access token within its result by combinding body, header, and secret key in jwt]
    """
    to_encode = data.copy()
    expire= datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt