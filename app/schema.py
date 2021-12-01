
from pydantic import BaseModel, errors, EmailStr
from datetime import datetime
from typing import NewType, Optional, List
from app.database import Base
from pydantic.types import conint #validate only 1 and below can be store

### validation class, make sure user pass in appropriate FIELDS before POST
### Schema to check field requirement and return 

class userlogin(BaseModel):
    email: EmailStr
    password: str

    
class ReturnUser(BaseModel):
    id : int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class schema(BaseModel):
    # id: Optional[int] = None    
    title: str
    content: str
    published: bool = True
        
class CheckPost(schema):
    pass

class ReturnPost(schema):
    id: int
    created_at: datetime
    owner_id : int
    owner_info: ReturnUser
    class Config:
        orm_mode = True
             
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class token(BaseModel):
    access_token : str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    
class PostOut(BaseModel):
    Post: ReturnPost
    votes: int
    
    class Config:
        orm_mode = True
        
    
    