from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import setting


<<<<<<< HEAD
SQLALCHEMY_DATABASE_URL = f'postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}'

=======
# SQLALCHEMY_DATABASE_URL =f'postgresql://{setting.database_username}:{setting.database_password}@{setting.database_port}/{setting.database_name}'
# hello world
SQLALCHEMY_DATABASE_URL=
>>>>>>> a4ad560f80e7e5e982bd6b3a5d361a505c3785bb

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
#         conn = psycopg2.connect(host= '', database='', user='', password='', cursor_factory=RealDictCursor)
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

