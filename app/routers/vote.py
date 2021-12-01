from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.sql.functions import user
from .. import schema, database, model, oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/vote',
    tags=['vote']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schema.Vote,
         db: Session = Depends(database.get_db),
        current_user: int = Depends(oauth2.get_current_user)):
    
    ## Check if post exist, if not raise exception
    post = db.query(model.Post).filter(model.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {vote.post_id} does not exist!')
    
    
    ### Check query if MODEL post_id and user_id same as INPUT post_id and user_id
    vote_query = db.query(model.Vote).filter(model.Vote.post_id == vote.post_id,
                                                 model.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    
    if (vote.dir == 1):
        ## If vote already found, reject that vote
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'user {current_user.id} has already voted on post {vote.post_id}')
        
        new_vote = model.Vote(post_id = vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {'message': 'Successfully added vote!'}
    
    else:
        ## if vote not found  raise, cant found the vote
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='vote does not exist!')
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        
        return {"message": "Successfully deleted vote!"}