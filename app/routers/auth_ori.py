from fastapi import APIRouter, Depends, status, HTTPException, Response
### for requirement of userinput space of username and password
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 
from sqlalchemy.orm import Session
from app import oauth2
from .. import database, schema, model, utils
 
router = APIRouter(tags=["Authentication"])

@router.post('/login')    ### Oauth2passwordreuqestform for demand of username and pass
def login_(credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    """ Take in user input credentials and check against database credentials for authentication 
    -   Oauth2passwordreuqestform for demand of username and pass
    -   verfipassword funcion for hashing password and compare with db password
    -   access_token, generate Secret token with signature using jwt, parameter passing for return when granted
    """
    # extract db email and validate first one matching with credentials email input
    user_name = db.query(model.User_).filter(
        model.User_.email == credentials.username).first()
    
    if not user_name:
        raise HTTPException(status_code=status.HTTP_403_NOT_FOUND, detail=f'invalid credentials')
    
    hashed_password = utils.verifypassword(credentials.password, user_name.password)
    
    if not hashed_password:
        raise HTTPException(status_code=status.HTTP_403_NOT_FOUND, detail=f'invalid credentials')
    
    
    access_token = oauth2.create_access_token(data={'user_id': user_name.id})
                                                    
    return {'access_token': access_token, 'token_type': 'bearer'}

