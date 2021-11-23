import requests

payload = ('tien', 5520)

r = requests.get('https://httpbin.org/basic-auth/tien/5520', auth=payload, timeout=5)

print(r)

my_dict = r.json()

print(my_dict['user'])
print(my_dict['authenticated'])
# with open('request_image.png', 'wb') as f:
#     f.write(r.content)