from enum import unique
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean
from .database import Base

### Use for design table and data modeling definition

class Post(Base):
    __tablename__ = 'Posts_table'
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    # owner_id = Column(Integer, ForeignKey("users_table.id"
    #                                     , ondelete="CASCADE")
    #                                     , nullable=False)
    # owner_info = relationship("User_")

    
# class User_(Base):
#     __tablename__ = 'users_table'
#     id = Column(Integer, primary_key=True, nullable=False)
#     email = Column(String, nullable=False, unique=True)
#     password = Column(String, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))


# class Vote(Base): # composite key of ID column from each tables
#     __tablename__='votes'
#     user_id = Column(Integer, ForeignKey("users_table.id",
#                                          ondelete="CASCADE"), primary_key=True)
#     post_id = Column(Integer, ForeignKey("Posts_table.id",
#                                          ondelete="CASCADE"),
#                                         primary_key=True)
                                        
    