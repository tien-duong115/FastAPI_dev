from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import database, schema, model, utils
 
router = APIRouter(tags=["Authentication"])

@router.post('/login')
def login_(credentials: schema.userlogin, db: Session = Depends(database.get_db)):
    """ Take in user input credentials and check against database credentials for authentication """
    
    # extract db email and validate first one matching with credentials email input
    user_name = db.query(model.User_).filter(
        model.User_.email == credentials.email).first()
    
    if not user_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credentials')
    
    hashed_password = utils.verifypassword(credentials.password, user_name.password)
    
    if not hashed_password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credentials')
    
    return {'token': 'some token'}

    
    