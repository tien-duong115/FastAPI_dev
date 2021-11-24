from .. import model, schema
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update
from ..database import  get_db
from typing import NewType, Optional, List


router = APIRouter()


def find_index_post(id):
    for i, p in enumerate():
        if p['id'] == id:
            return i


@router.get('/posts', response_model=List[schema.ReturnPost])
def get_post(db: Session = Depends(get_db)):
    post = db.query(model.Post).all()
    p_post = db.query(model.Post)
    print('>>> ', p_post)
    return post


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schema.ReturnPost)
def create_posts(post: schema.CheckPost, db: Session = Depends(get_db)):
    new_post = model.Post(**post.dict())    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/posts/{id}", response_model=schema.ReturnPost)
def get_one_post(id: int, db: Session = Depends(get_db)):
    p_post = db.query(model.Post).filter(model.Post.id == id)
    print('>>> ', p_post)
    post = db.query(model.Post).filter(model.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id: {id} was not found!')
    return post

# @router.delete('/posts/{id}', response_model=schema.ReturnPost)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     cursor.execute(""" DELETE FROM post WHERE id = %s returning * """, (str(id)))
#     delete_post = cursor.fetchone()
#     conn.commit()
#     if delete_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with {id} was not Found!')
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @router.delete('posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
    
#     post = db.query(model.Post).filter(model.Post.id == id)
#     print(post)
#     if post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'post with {id} was not Found!')
#     post.delete(synchronize_session=False)
    
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/posts/{id}", response_model=schema.schema)
def update_post(id: int, post: schema.CheckPost,  db: Session = Depends(get_db)):
    updated_post = db.query(model.Post).filter(model.Post.id == id)
    if updated_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not found!')
    updated_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return  updated_post.first()

