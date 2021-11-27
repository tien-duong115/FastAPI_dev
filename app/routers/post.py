from pydantic.main import SchemaExtraCallable
from .. import model, schema, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update
from ..database import  get_db
from typing import NewType, Optional, List

router = APIRouter(
    prefix='/posts',
    tags=['posts']   ## grouping into each section on UI
)

### Router object for post API

@router.get('/', response_model=List[schema.ReturnPost])
def get_post(db: Session = Depends(get_db)):
    
    post = db.query(model.Post).all()
    p_post = db.query(model.Post)
    print('>>> ', p_post)
    return post


@router.get('/all', response_model=List[schema.ReturnPost])
def get_AllPost_ByUser(db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)):
    
    post = db.query(model.Post).filter(model.Post.owner_id == current_user.id).all()
    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.ReturnPost)
def create_posts(post: schema.CheckPost, 
                 db: Session = Depends(get_db), 
                 current_user: int = Depends(oauth2.get_current_user)):
    
    new_post = model.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schema.ReturnPost)
def get_one_post(id: int, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):
    
    p_post = db.query(model.Post).filter(model.Post.id == id)
    print('>>> ', p_post)
    post = db.query(model.Post).filter(model.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id: {id} was not found!')
    return post


@router.put("/{id}", response_model=schema.ReturnPost)
def update_post(id: int, updated_post: schema.CheckPost, 
                db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    """
    Update a post with matching ID,
    Post only authenticate if ID are matching
    """
    post_1 = db.query(model.Post).filter(model.Post.id == id)
    post_2 = post_1.first()

    if post_1 == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
  
    if post_2.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_1.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return post_2


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT )
def delete_post(id: int, 
                db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    
    post_1 = db.query(model.Post).filter(model.Post.id == id)
    post_2 = post_1.first()
    
    if post_1 == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post_2.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, details='Not authroize as User!')
    
    post_1.delete(synchronize_session=False)
    
    db.commit()
    
    return Response(status_code=status.HTTP_202_ACCEPTED), print()
    
    
    
    







# @router.put("/{id}", response_model=schema.schema)
# def update_post(id: int, post: schema.CheckPost,
#                 db: Session = Depends(get_db)):
    
#     updated_post = db.query(model.Post).filter(model.Post.id == id)
    
#     if updated_post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not found!')
#     updated_post.update(post.dict(), synchronize_session=False)
    
#     db.commit()
    
#     return  updated_post.first()


# @router.delete('/{id}', response_model=schema.ReturnPost)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     cursor.execute(""" DELETE FROM post WHERE id = %s returning * """, (str(id)))
#     delete_post = cursor.fetchone()
#     conn.commit()
#     if delete_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with {id} was not Found!')
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @router.delete(/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
    
#     post = db.query(model.Post).filter(model.Post.id == id)
#     print(post)
#     if post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'post with {id} was not Found!')
#     post.delete(synchronize_session=False)
    
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)



