import requests
import random
import json
from datetime import datetime
from db import Global, con

con()

d = Global.select().where(Global.user_id == 650358102)[0].license - datetime.today()
#mm, ss = divmod(d.seconds, 60)
#hh, mm = divmod(mm, 60)
print(d.days)


# url = f'https://sms.ru/sms/send?api_id=E996BF89-7113-F21D-D4D2-E6589388D3A0&to=79025864383&msg=Здравствуйте, молодой чебурек&json=0'
# response = requests.get(url)
# balance = re.findall(r'balance=(\w+)', str(response.text.encode('utf8')))[0]
# print(balance)

