
my_post = [{'title': 'this is the title', 'content': 'This is the content', 'id': 1}, {'title':'favorite food', 'content': 'pizza', 'id': 2}]

def find_post(id):
    for p in my_post:
        if p['id'] == id:
            return p


# def find_index_post(id):
#     for i, p in enumerate(my_post):
#         # if p['id'] == id:
#         #     return id

for i, p in enumerate(my_post):
    print(p['id'])

