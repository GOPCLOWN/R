from db import Global, WhiteNumber
import urllib.request
import json
from bs4 import BeautifulSoup as bs
import requests
from datetime import timedelta, datetime


def CountUser():
    allUsers = Global.select().count()
    userBuy = Global.select().where(Global.license != '').count()
    userFree = Global.select().where(Global.license == '').count()
    return f'Количество пользователей: {allUsers} \nКупили приват: {userBuy}\nНе купили приват: {userFree}\nАтакуют: attack'


def getContact(number):
    try:
        num_name = []
        phone_ow = requests.get(f'https://phonebook.space/?number=%2B{number}').text
        content = bs(phone_ow, 'html.parser').find('div', class_='results')
        for i in content.find_all('li'):
            num_name.append(i.text.strip())
        if not num_name:
            return f'[+] Теги по номеру: Нечего нет'
        else:
            return '[+]'+' Теги с номера: '+', '.join(num_name)
    except requests.exceptions.RequestException:
        return 'Произошла ошибка'


def informNumber(phone, send, chat_id, key):
    getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=79227299015"
    try:
        infoPhone = urllib.request.urlopen(getInfo)
    except:
        return 'Проблема с поиском номера'
    infoPhone = json.load(infoPhone)
    send(chat_id, f"""Номер сотового: {phone}
Страна: {infoPhone["country"]["name"]}
Регион: {infoPhone["region"]["name"]}
Округ: {infoPhone["region"]["okrug"]}
Оператор: {infoPhone["0"]["oper"]} 
Часть света: {infoPhone["country"]["location"]}
------------------------------
{getContact(phone)}
""", reply_markup=key)


def buySubs(count, user_id, cost):
    user = Global.select().where(Global.user_id == user_id)
    if user[0].balance >= int(cost):
        Global.update(balance=Global.balance - int(cost)).where(Global.user_id == user_id).execute()
        if user[0].license == '':
            give = datetime.now() + timedelta(days=int(count))
            Global.update(license=give).where(Global.user_id == user_id).execute()
            return f'[✅]Вы успешно приобрели лицензию на {count} дн(я/ей)'
        else:
            give = user[0].license + timedelta(days=int(count))
            Global.update(license=give).where(Global.user_id == user_id).execute()
            return f'[✅]Вы успешно приобрели лицензию на {count} дн(я/ей)'
    else:
        return f'[🚫]У вас недостаточно средств\n[💵]Ваш баланс: {user[0].balance}'


def statik(attack):
    f = open('proxy/proxy.txt', 'rb')
    proxy = len(f.readlines())
    f.close()
    allUsers = Global.select().count()
    allNumber = WhiteNumber.select().count()
    return f"""
🌪Количество сервисов RU: 40
🙍‍Всего пользователей: {allUsers}
⚡Всего прокси: {proxy}
💣В данный момент атакуют: {len(attack)}
🌞Номеров в белом листе: {allNumber}
"""