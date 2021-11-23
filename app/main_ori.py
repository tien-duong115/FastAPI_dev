from typing import NewType, Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel, errors
from random import randrange
from requests.api import post
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# validation class, make sure user pass in appropriate FIELDS before POST
class schema(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None    



counter = 0


def find_index_post(id):
    for i, p in enumerate():
        if p['id'] == id:
            return i

while True: 
    try:
        conn = psycopg2.connect(host= 'localhost', database='FastAPI_db', user='postgres', password='password', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Datase connection success!!!')
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
        

FirstAPI = FastAPI() 


@FirstAPI.get('/posts')
def get_post():
    cursor.execute(""" SELECT * FROM products """)
    post = cursor.fetchall()
    conn.commit()
    return post


@FirstAPI.post("/posts")
def create_posts(post: schema):
    cursor.execute(""" INSERT INTO products (title, content, published) VALUES (%s, %s, %s) RETURNING *""", \
        (post.title, post.content, post.published))
    new_post = cursor.fetchall()
    conn.commit()
    return {'new_post: ': new_post}


@FirstAPI.get("/posts/{id}")
def get_one_post(id: int, response: Response):
    cursor.execute(""" SELECT * FROM products WHERE id = %s """, (str(id),))
    post = cursor.fetchone()
    conn.commit()
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f'post with {id} was not Found!'}
    return {'post_detail': post}


@FirstAPI.delete('post/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(""" DELETE FROM post WHERE id = %s returning * """, (str(id)))
    delete_post = cursor.fetchone()
    conn.commit()
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with {id} was not Found!')
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@FirstAPI.put("/posts/{id}")
def update_post(id: int, post: schema):
    cursor.execute(""" UPDATE products SET title = %s, content = %s, published = %s \
        WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id) ))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not found!')
    return {'data': 'success'}
 

# my_post = [{'title': 'this is the title 1', 'content': 'This is the content 1', 'id': 1}, {'title':'favorite food', 'content': 'pizza', 'id': 2}]



# Chronoligical order does matter 
# REQUEST get method url: "/"

# @FirstAPI.get('/')
# def root():
#     return {'id': '654-220-2299', 'mainframe':'timeout!'}


# @FirstAPI.post('/post_request')
# def post_request(payload: dict = Body(...)):
#     return {"new_post": \
#         f"title: {payload['title']}, \
#         content: {payload['content']}"}


# @FirstAPI.get('/posts/latest')
# def get_latest_post():
#     post = my_post[len(my_post)-1]
#     return {'detail': post}

# @FirstAPI.get("/posts/{id}")
# def create_posts(id: int, response: Response):
#     post = find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with {id} was not Found!')
#     return {'post_detail': post}



# @FirstAPI.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
# def delete_posts(id: int):
#     index = find_index_post(id)
    
#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not found!')
    
    
#     my_post.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @FirstAPI.put("/posts/{id}")
# def update_post(id: int, post: schema):
    
#     index = find_index_post(id)
    
#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} does not found!')
    
#     post_dict = post.dict()
#     post_dict['id'] = id
#     my_post[index] = post_dict
#     return {'data': post_dict}
 