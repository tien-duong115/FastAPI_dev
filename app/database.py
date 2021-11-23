from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL ='postgresql://postgres:password@localhost/FastAPI_db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

### Generate sqlalchemy session along with posgresql DB

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

