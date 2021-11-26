from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from jose.constants import Algorithms
from sqlalchemy import schema
from sqlalchemy.orm import Session
from . import schema, database, model


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# def create_access_token(data:dict):
#     """[Generate access token with HS256]

#     Args:
#         data (dict): [return secret token]

#     Returns:
#         [dict]: [return a dictionary of access token within its result by combinding body, header, and secret key in jwt]
#     """
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({'exp': expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schema.TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data
# def verify_access_token(token: str, credentials_exception):
#     try:
        
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[Algorithms])
        
#         id : str = payload.get('user_id')
#         if id is None:
#             raise credentials_exception
#         token_data = schema.TokenData(id=id)

#     except JWTError:
#         raise credentials_exception
#     return token_data



def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    
    token = verify_access_token(token, credentials_exception)
    user = db.query(model.User_).filter(model.User_.id == token.id).first()

    return user

# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
#     credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
#                                           detail=f"could not validate credentials", headers={'WWW-Authenticate': 'Bearer'})
#     token = verify_access_token(token, credentials_exception)

#     user = db.query(model.User_).filter(model.User_.id == token.id).first()

#     return user    
