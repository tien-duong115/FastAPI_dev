from typing import NewType, Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
from passlib.utils.decor import deprecated_function
from requests import sessions
from requests.api import post
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update
from .database import engine, sessionLocal, get_db
from . import model, schema, utils
from .routers import post, users, auth ### import router object from router folder

### Bind sqlalchemy object and database schema from model file
model.Base.metadata.create_all(bind=engine) 

FirstAPI = FastAPI() ### Generate FastAPI object
FirstAPI.include_router(post.router) ### included router object into FirstAPI object
FirstAPI.include_router(users.router)
FirstAPI.include_router(auth.router)

def find_index_post(id): ### function to find specific ID
    for i, p in enumerate():
        if p['id'] == id:
            return i


counter = 0
while True:  ### Connection template to connect with Postgres
    try:
        conn = psycopg2.connect(host= '', database='', user='', password='', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('>>> Datase connection success!!!')
        break
    except Exception as e:
        print('connection to database failed!!')
        print(f'Number of try: {counter}, still receive error!', e)
        time.sleep(2)
        counter += 1

        if counter == 5:
            print(f'Tried {counter}, give up.')
            break
        print(counter)














# GET method, get all Post using ORM, without worry with SQL lang
# @FirstAPI.get('/sqlalchemy')
# def test_posts(db: Session = Depends(get_db)):
#     post = db.query(model.Post).all()
#     p_post = db.query(model.Post)
#     print('>>> ', p_post)
#     return {'data return': post}

# Get post with ORM connect with db session and model

# @FirstAPI.get('/posts', response_model=List[schema.ReturnPost])
# def get_post(db: Session = Depends(get_db)):
#     post = db.query(model.Post).all()
#     p_post = db.query(model.Post)
#     print('>>> ', p_post)
#     return post


# @FirstAPI.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schema.ReturnPost)
# def create_posts(post: schema.CheckPost, db: Session = Depends(get_db)):
#     new_post = model.Post(**post.dict())    
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post


# @FirstAPI.get("/posts/{id}", response_model=schema.ReturnPost)
# def get_one_post(id: int, db: Session = Depends(get_db)):
#     p_post = db.query(model.Post).filter(model.Post.id == id)
#     print('>>> ', p_post)
#     post = db.query(model.Post).filter(model.Post.id == id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f'post with id: {id} was not found!')
#     return post

# @FirstAPI.delete('/posts/{id}', response_model=schema.ReturnPost)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     cursor.execute(""" DELETE FROM post WHERE id = %s returning * """, (str(id)))
#     delete_post = cursor.fetchone()
#     conn.commit()
#     if delete_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with {id} was not Found!')
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# # @FirstAPI.delete('posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
# # def delete_post(id: int, db: Session = Depends(get_db)):
    
# #     post = db.query(model.Post).filter(model.Post.id == id)
# #     print(post)
# #     if post.first() == None:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail=f'post with {id} was not Found!')
# #     post.delete(synchronize_session=False)
    
# #     db.commit()
# #     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @FirstAPI.put("/posts/{id}", response_model=schema.schema)
# def update_post(id: int, post: schema.CheckPost,  db: Session = Depends(get_db)):
#     updated_post = db.query(model.Post).filter(model.Post.id == id)
#     if updated_post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not found!')
#     updated_post.update(post.dict(), synchronize_session=False)
#     db.commit()
#     return  updated_post.first()


# ### User_table API From Here ###
# @FirstAPI.post("/users", status_code=status.HTTP_201_CREATED, response_model=schema.ReturnUser)
# def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
#     user.password =  utils.hash(user.password) ## hashed password
#     new_user = model.User_(**user.dict())    
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @FirstAPI.get("/users", response_model=List[schema.ReturnUser])
# def get_all_users(db: Session = Depends(get_db)):
#     get_user = db.query(model.User_).all()    
#     p_user = db.query(model.User_)
#     print('>>> ', p_user)
#     return get_user


# @FirstAPI.get("/users/{id}", response_model=schema.ReturnUser)
# def get_one_users(id: int ,db: Session = Depends(get_db)):
#     get_user = db.query(model.User_).filter(model.User_.id == id).first()
#     if not get_user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f'post with id: {id} does not found!')
#     return get_user
    