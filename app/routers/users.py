from .. import model, schema, utils
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update
from ..database import  get_db
from typing import NewType, Optional, List

router = APIRouter()

### User_table API From Here ###
@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schema.ReturnUser)

def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    user.password =  utils.hash(user.password) ## hashed password
    new_user = model.User_(**user.dict())    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users", response_model=List[schema.ReturnUser])
def get_all_users(db: Session = Depends(get_db)):
    get_user = db.query(model.User_).all()    
    p_user = db.query(model.User_)
    print('>>> ', p_user)
    return get_user


@router.get("/users/{id}", response_model=schema.ReturnUser)
def get_one_users(id: int ,db: Session = Depends(get_db)):
    get_user = db.query(model.User_).filter(model.User_.id == id).first()
    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id: {id} does not found!')
    return get_user
    