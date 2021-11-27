
from pydantic import BaseModel, errors, EmailStr
from datetime import datetime
from typing import NewType, Optional, List

from app.database import Base

### validation class, make sure user pass in appropriate FIELDS before POST
### Schema to check field requirement and return 

class schema(BaseModel):
    # id: Optional[int] = None    
    title: str
    content: str
    published: bool = True
    
class CheckPost(schema):
    owner_id: int

class ReturnPost(CheckPost):
    id: int
    created_at: datetime
    owner_id : int
    class Config:
        orm_mode = True
             
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class ReturnUser(BaseModel):
    id : int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True
        
class userlogin(BaseModel):
    email: EmailStr
    password: str
    
class token(BaseModel):
    access_token : str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    