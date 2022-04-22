import os
import requests
import json

result = requests.get("https://reqres.in/api/users?page=2").json() # dict
new = result["data"] # list users
path = os.getcwd() # current directory
for i in range(0, len(new)):
    folder  = str(new[0]['id'])
    with open(path + folder )
with open(path + '/text_' ,'w') as file:

file.write('fsdf')
for human in new:
    print(human["id"])



'''
with open('text1.txt', 'w') as file:
    file.write(result)
os.path.join(mypath, filename)
with open('text1.txt', 'r') as file:
    list_all_users = json.loads(file.read())['data']
'''

'''print(os.getcwd())
os.mkdir('users_data')'''

'''import requests
from bs4 import BeautifulSoup
link = 'https://browser-info.ru/'
response = requests.get(link)p
soup  = BeautifulSoup(response.text, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])


'''