from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL ='postgresql://postgres:password@localhost/FastAPI_db'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

### Generate sqlalchemy session along with posgresql DB
Base=declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()



# counter = 0
# while True:  ### Connection template to connect with Postgres
#     try:
#         conn = psycopg2.connect(host= 'localhost', database='FastAPI_db', user='postgres', password='password', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('>>> Datase connection success!!!')
#         break
#     except Exception as e:
#         print('connection to database failed!!')
#         print(f'Number of try: {counter}, still receive error!', e)
#         time.sleep(2)
#         counter += 1

#         if counter == 5:
#             print(f'Tried {counter}, give up.')
#             break
#         print(counter)

