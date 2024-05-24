import requests
from pprint import pprint
r = {'title':'t','description':'d'}

uri = 'http://127.0.0.1:5000/todo/api/v1.0/task/'
#resg = requests.get(uri+'0')                     #200
#resp = requests.post(uri+'0',json=r)             #200
#resd = requests.delete(uri+'2')                  #200       
#respu = requests.put(uri+'1',json={'title':'2'}) #200
print(res.status_code)
pprint(res.json())