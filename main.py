import telebot
from service import Spam
import os
from threading import Thread
from datetime import datetime, timedelta
from config import token, admin_id
from db import con, Global, WhiteNumber
import keyboard
import text
import time
import psutil as ps
import function
from proxy.proxyParsing import ParsingProxy

con()

startime = datetime.now()


class Telegs:
    def __init__(self, token, admin_id):
        self.admin_id = admin_id
        self.bot = telebot.TeleBot(token)
        self.send = self.bot.send_message
        self.next = self.bot.register_next_step_handler
        self.attack = []
        self.proxys = []

        @self.bot.message_handler(commands=['start'])
        def start(message):
            userInfo = Global.select().where(Global.user_id == message.from_user.id)
            chat_id = message.from_user.id
            if userInfo.exists():
                if userInfo[0].adm:
                    self.send(chat_id, 'Для управления ботом воспользуйтесь кнопками',
                              reply_markup=keyboard.userPanelAdm)
                else:
                    if chat_id == admin_id:
                        self.send(chat_id, 'Для управления ботом воспользуйтесь кнопками',
                                  reply_markup=keyboard.userPanelAdm)
                        Global.update(adm=True).where(Global.user_id == chat_id).execute()
                    else:
                        self.send(chat_id, 'Для управления ботом воспользуйтесь кнопками',
                                  reply_markup=keyboard.userPanel)
            else:
                Global.create(
                    user_id=chat_id,
                )
                self.send(chat_id, 'Введите команду /start еще раз')

        @self.bot.message_handler(content_types=['text'])
        def bot_one(message):
            userInfo = Global.select().where(Global.user_id == message.from_user.id)
            chat_id = message.from_user.id
            if userInfo.exists():
                chat_id = message.from_user.id
                if message.text == '💌SmS':
                    if userInfo[0].license == '':
                        self.send(chat_id, '[🚫]У вас нету лицензии')
                    else:
                        if userInfo[0].license > datetime.now():
                            if os.stat('proxy/proxy.txt').st_size > 0:
                                start = self.send(chat_id,
                                                  '[✅]Введите номер с 7 и кол-во циклов через пробел\nПример 79999999999 60: ', reply_markup=keyboard.cancelButton2)
                                self.bot.register_next_step_handler(start, self.startSpam)
                            else:
                                self.send(chat_id, '[🚫]Подождите, идет обновление прокси!')
                        else:
                            Global.update(license='').where(Global.user_id == message.from_user.id).execute()
                            self.send(chat_id, '[🚫]У вас закончилась лицензия')
                elif message.text == '🔥Начать спам':
                    self.send(chat_id, '[✅]Выберите режим отправки', reply_markup=keyboard.startSpam)
                elif message.text == '🙎Профиль':
                    if userInfo[0].license == '':
                        self.send(chat_id, text.profileNone.replace('{bal}', str(userInfo[0].balance)).replace('{id}', str(userInfo[0].id)).replace('{user_id}', str(userInfo[0].user_id)), parse_mode='HTML')
                    else:
                        day = userInfo[0].license - datetime.today()
                        self.send(chat_id, text.profile
                                  .replace('{bal}', str(userInfo[0].balance)).replace('{id}', str(userInfo[0].id)).replace('{user_id}', str(userInfo[0].user_id)).replace('{license}', str(day.days)), parse_mode='HTML')
                elif message.text == '👌SmS со своим текстом':
                    self.send(chat_id, '[❗]Функция в разработке')
                elif message.text == '📞Call':
                    self.send(chat_id, '[❗]Функция в разработке')
                elif message.text == '💡Белый лист':
                    if userInfo[0].license != '':
                        if userInfo[0].license > datetime.now():
                            self.send(chat_id, '[✅]Вы вошли в управление белым листом', reply_markup=keyboard.whiteList)
                        else:
                            Global.update(license='').where(Global.user_id == message.from_user.id).execute()
                            self.send(chat_id, '[🚫]У вас закончилась лицензия')
                    else:
                        self.send(chat_id, '[🚫]Чтобы использовать эту функцию необходимо приобрести подписку')
                elif message.text == '🔒Добавить':
                    number = self.send(chat_id, '[✅]Введите номер с 7: ')
                    self.bot.register_next_step_handler(number, self.addWhite)
                elif message.text == '🔓Удалить':
                    number = self.send(chat_id, '[✅]Введите номер с 7: ')
                    self.bot.register_next_step_handler(number, self.delWhite)
                elif message.text == '❌Выйти❌':
                    if userInfo[0].adm:
                        self.send(chat_id, '[🚫]Вы вышли в основное меню', reply_markup=keyboard.userPanelAdm)
                    else:
                        self.send(chat_id, '[🚫]Вы вышли в основное меню', reply_markup=keyboard.userPanel)
                elif message.text == '👑Деанон':
                    if userInfo[0].license != '':
                        if userInfo[0].license > datetime.now():
                            num = self.send(chat_id, '[✅]Введите номер телефона: ')
                            self.bot.register_next_step_handler(num, self.InformPhone)
                    else:
                        self.send(chat_id, '[🚫]Для доступа к данной функции требуется лицензия')
                elif message.text == '😎Подписки':
                    self.send(chat_id, '[✅]Выберите подписку[✅]', reply_markup=keyboard.subscription)
                elif message.text == '💸Статистика':
                    self.send(chat_id, function.statik(self.attack))
                else:
                    if userInfo[0].adm:
                        adminCommand(message, userInfo, chat_id)
                    elif chat_id == admin_id:
                        adminCommand(message, userInfo, chat_id)
                    else:
                        self.send(chat_id, '[❗]Я не понял вашу команду!')
            else:
                self.send(chat_id, '[❗]Введите команду /start')

        def adminCommand(message, userInfo, chat_id):
            if message.text == 'Выдать лицензию':
                reg = self.send(chat_id, '[✅]Введите Id пользователя: ', reply_markup=keyboard.cancelButton)
                self.next(reg, self.giveLicense_1)
            elif message.text == 'Выдать баланс':
                addBalance = self.send(chat_id, '[✅]Введите id пользователя: ', reply_markup=keyboard.cancelButton)
                self.bot.register_next_step_handler(addBalance, self.giveBalanceFirst)
            elif message.text == 'Забрать баланс':
                delBalance = self.send(chat_id, '[✅]Введите id пользователя: ', reply_markup=keyboard.cancelButton)
                self.bot.register_next_step_handler(delBalance, self.delBalanceFirst)
            elif message.text == '🥇Админ-панель🥇':
                self.send(chat_id, '[✅]Успешный доступ в Админ-панель', reply_markup=keyboard.adminPanel)
            elif message.text == 'Назад':
                self.send(chat_id, '[✅]Вы успешно вернулись назад', reply_markup=keyboard.userPanelAdm)
            elif message.text == 'Обновить прокси':
                Thread(target=ParsingProxy, args=(self.send, chat_id)).start()
            elif message.text == 'Забрать лицензию':
                delLicense = self.send(chat_id, '[✅]Введите id пользователя: ', reply_markup=keyboard.cancelButton)
                self.bot.register_next_step_handler(delLicense, self.deleteLicense)
            elif message.text == 'Статистика':
                self.send(chat_id, function.CountUser().replace('attack', str(len(self.attack))))
            elif message.text == 'Сервер':
                self.send(chat_id, self.serverInform())

        @self.bot.callback_query_handler(func=lambda c: True)
        def inline(c):
            buy = telebot.types.InlineKeyboardMarkup(row_width=1)
            buy1 = telebot.types.InlineKeyboardButton(text='Подтвердить', callback_data=f'buy {c.data}')
            cancel = telebot.types.InlineKeyboardButton(text='Назад', callback_data=f'back')
            buy.add(buy1, cancel)
            if c.data == '1d':
                self.bot.edit_message_text(chat_id=c.from_user.id, message_id=c.message.message_id, text='[✅]Вы уверены что хотите приобрести подписку на 1 день за 10 рублей?\nС вашего баланса спишется 10 рублей', reply_markup=buy)
            elif c.data == '7d':
                self.bot.edit_message_text(chat_id=c.from_user.id, message_id=c.message.message_id, text='[✅]Вы уверены что хотите приобрести подписку на 7 дней за 50 рублей?\nС вашего баланса спишется 50 рублей', reply_markup=buy)
            elif c.data == '14d':
                self.bot.edit_message_text(chat_id=c.from_user.id, message_id=c.message.message_id, text='[✅]Вы уверены что хотите приобрести подписку на 14 дней за 100 рублей?\nС вашего баланса спишется 100 рублей', reply_markup=buy)
            elif c.data == '30d':
                self.bot.edit_message_text(chat_id=c.from_user.id, message_id=c.message.message_id, text='[✅]Вы уверены что хотите приобрести подписку на 30 дней за 150 рублей?\nС вашего баланса спишется 150 рублей', reply_markup=buy)
            elif c.data == 'always':
                self.bot.edit_message_text(chat_id=c.from_user.id, message_id=c.message.message_id, text='[✅]Вы уверены что хотите приобрести подписку навсегда за 300 рублей?\nС вашего баланса спишется 300 рублей', reply_markup=buy)
            elif c.data == 'back':
                self.bot.edit_message_text(chat_id=c.from_user.id, message_id=c.message.message_id, text='Выберите подписку', reply_markup=keyboard.subscription)
            elif 'buy' in c.data:
                c.data = c.data.replace('buy ', '')
                if c.data == '1d':
                    self.bot.edit_message_text(chat_id=c.from_user.id, message_id=c.message.message_id, text=function.buySubs(1, c.from_user.id, 10))
                elif c.data == '7d':
                    self.bot.edit_message_text(chat_id=c.from_user.id, message_id=c.message.message_id, text=function.buySubs(7, c.from_user.id, 50))
                elif c.data == '14d':
                    self.bot.edit_message_text(chat_id=c.from_user.id, message_id=c.message.message_id, text=function.buySubs(14, c.from_user.id, 100))
                elif c.data == '30d':
                    self.bot.edit_message_text(chat_id=c.from_user.id, message_id=c.message.message_id, text=function.buySubs(30, c.from_user.id, 150))
                elif c.data == 'always':
                    self.bot.edit_message_text(chat_id=c.from_user.id, message_id=c.message.message_id, text=function.buySubs(9999, c.from_user.id, 300))
        while True:
            try:
                self.bot.infinity_polling()
            except Exception as e:
                self.send(admin_id, f'Бот умер: {e}')

    def serverInform(self):
        threads = ps.cpu_count(logical=False)
        lthreads = ps.cpu_count()
        RAM = ps.virtual_memory().percent
        cpu_percents = ps.cpu_percent(percpu=True)
        starttime = datetime.now() - startime
        cpupercents = ""
        for a in range(lthreads):
            cpupercents += "Поток : {} | Загруженность : {} %\n".format(a + 1, cpu_percents[a - 1])
        return """Загрузка систем :
Ядер : {} | Загруженность : {}%
{}Загруженность ОЗУ : {} %
Времени прошло со старта : {} """.format(threads, ps.cpu_percent(), cpupercents, RAM,
                                                   "{} дней, {} часов, {} минут.".format(starttime.days,
                                                                                               starttime.seconds // 3600,
                                                                                               (
                                                                                                       starttime.seconds % 3600) // 60))

    def addWhite(self, message):
        print(message.text)
        if message.text[0] == '7':
            if message.text.isdigit():
                WhiteNumber.create(
                    user_id=message.from_user.id,
                    number=message.text
                )
                self.send(message.from_user.id, f'[✅]Номер {message.text} успешно добавлен в белый лист')
        else:
            self.send(message.from_user.id, '[🚫]Номер должен начинаться с 7! Повторите команду')

    def delWhite(self, message):
        if message.text[0] == '7':
            if message.text.isdigit():
                if WhiteNumber.select().where(WhiteNumber.number == message.text).exists():
                    if WhiteNumber.select().where(WhiteNumber.number == message.text)[0].user_id == message.from_user.id:
                        WhiteNumber.delete().where(WhiteNumber.number == message.text).execute()
                        self.send(message.from_user.id, f'[✅]Номер {message.text} успешно удален из белого листа')
                    else:
                        self.send(message.from_user.id, '[🚫]Нельзя удалить номер добавленный другим человеком')
                else:
                    self.send(message.from_user.id, '[🚫]Номер нет в белом листе!')
            else:
                self.send(message.from_user.id, '[🚫]Номер должен состоять из цифр!')
        else:
            self.send(message.from_user.id, '[🚫]Номер должен начинаться с 7! Повторите команду')

    def delBalanceFirst(self, message):
        if message.text.isdigit():
            user = Global.select().where(Global.user_id == message.text)
            if user.exists():
                addBalance = self.send(message.from_user.id, f'Баланс пользователя: {user[0].balance}\nА теперь введите сумму: ')
                self.bot.register_next_step_handler(addBalance, self.delBalanceTwo, message.text)
            else:
                self.send(message.from_user.id, '[🚫]Пользователя не существует', reply_markup=keyboard.adminPanel)
        elif message.text == '💢Отмена💢':
            self.send(message.from_user.id, '[❗]Действие отменено', reply_markup=keyboard.adminPanel)
        else:
            self.send(message.from_user.id, '[❗]Id пользователя состоит из цифр', reply_markup=keyboard.adminPanel)

    def delBalanceTwo(self, message, user_id):
        if message.text.isdigit():
            user = Global.select().where(Global.user_id == user_id)
            if user[0].balance >= int(message.text):
                Global.update(balance=Global.balance - int(message.text)).where(Global.user_id == user_id).execute()
                self.send(message.from_user.id, f'[✅]Вы успешно забрали {message.text} рублей у пользователя')
            else:
                self.send(message.from_user.id, f'[🚫]У пользователя {user_id} не достаточно денег\nБаланс пользователя: {user[0].balance}', reply_markup=keyboard.adminPanel)
        elif message.text == '💢Отмена💢':
            self.send(message.from_user.id, '[❗]Действие отменено', reply_markup=keyboard.adminPanel)
        else:
            self.send(message.from_user.id, '[❗]Сумма состоит из цифр', reply_markup=keyboard.adminPanel)

    def giveBalanceFirst(self, message):
        if message.text.isdigit():
            if Global.select().where(Global.user_id == message.text).exists():
                addBalance = self.send(message.from_user.id, 'А теперь введите сумму: ')
                self.bot.register_next_step_handler(addBalance, self.giveBalanceTwo, message.text)
            else:
                self.send(message.from_user.id, '[🚫]Пользователя не существует', reply_markup=keyboard.adminPanel)
        elif message.text == '💢Отмена💢':
            self.send(message.from_user.id, '[❗]Действие отменено', reply_markup=keyboard.adminPanel)
        else:
            self.send(message.from_user.id, '[❗]Id пользователя состоит из цифр', reply_markup=keyboard.adminPanel)

    def giveBalanceTwo(self, message, user_id):
        if message.text.isdigit():
            Global.update(balance=Global.balance + int(message.text)).where(Global.user_id == user_id).execute()
            self.send(message.from_user.id, f'[✅]Вы успешно выдали баланс пользователю {user_id}\nВыдали: {message.text}', reply_markup=keyboard.adminPanel)
            try:
                self.send(user_id, f'[✅]Вам выдали {message.text} рублей на баланс')
            except Exception as e:
                pass
        elif message.text == '💢Отмена💢':
            self.send(message.from_user.id, '[❗]Действие отменено', reply_markup=keyboard.adminPanel)
        else:
            self.send(message.from_user.id, '[❗]Сумма состоит из цифр', reply_markup=keyboard.adminPanel)

    def text_sms_one(self, message):
        if message.text[0] == '7':
            if message.text.isdigit() and len(message.text) == 11:
                pass
            else:
                pass


    def giveLicense_1(self, message):
        if message.text.isdigit():
            reg_2 = self.send(message.from_user.id, 'А теперь введите количество дней: ')
            self.next(reg_2, self.giveLicense_2, message.text)
        elif message.text == '💢Отмена💢':
            self.send(message.from_user.id, '[❗]Действие отменено', reply_markup=keyboard.adminPanel)
        else:
            self.send(message.from_user.id, '[🚫]Id пользователя состоит из цифр. Повторите команду!', reply_markup=keyboard.adminPanel)

    def giveLicense_2(self, message, user_id):
        if message.text.isdigit():
            userGive = Global.select().where(Global.user_id == user_id)
            if userGive.execute():
                if userGive[0].license == '':
                    give = datetime.now() + timedelta(days=int(message.text))
                    Global.update(license=give).where(Global.user_id == user_id).execute()
                    self.send(message.from_user.id,
                              f'[✅]Вы успешно выдали пользователю {user_id} лицензию на {message.text} дн(я/ей)', reply_markup=keyboard.adminPanel)
                    try:
                        self.send(user_id, f'[✅]Вам выдали лицензию на {message.text} дн(я/ей)')
                    except:
                        pass
                else:
                    give = userGive[0].license + timedelta(days=int(message.text))
                    Global.update(license=give).where(Global.user_id == user_id).execute()
                    self.send(message.from_user.id,
                              f'[✅]Вы успешно добавили пользователю {user_id} лицензию на {message.text} дн(я/ей)',
                              reply_markup=keyboard.adminPanel)
                    try:
                        self.send(user_id, f'[✅]Вам добавили лицензию на {message.text} дн(я/ей)')
                    except:
                        pass
            else:
                self.send(message.from_user.id, '[🚫]Пользователя не существует!', reply_markup=keyboard.adminPanel)
        elif message.text == '💢Отмена💢':
            self.send(message.from_user.id, '[❗]Действие отменено', reply_markup=keyboard.adminPanel)
        else:
            self.send(message.from_user.id, '[🚫]Кол-во дней состоит из цифр. Повторите команду!', reply_markup=keyboard.adminPanel)

    def InformPhone(self, message):
        if message.text[0] == '7':
            if message.text.isdigit():
                openAvito = telebot.types.InlineKeyboardMarkup(row_width=1)
                link = telebot.types.InlineKeyboardButton(text='Поиск в Whats app',
                                                          url='https://api.whatsapp.com/send?phone=+{}'.format(
                                                              message.text))
                openAvito.add(link)
                self.send(message.from_user.id, '[❗]Ожидайте результатов идет поиск')
                Thread(target=function.informNumber, args=(message.text, self.send, message.from_user.id, openAvito)).start()
        else:
            self.send(message.from_user.id, '[❗]Номер телефона должен начинаться с 7')

    def deleteLicense(self, message):
        if message.text.isdigit():
            info = Global.select().where(Global.user_id == message.text)
            if info.exists():
                Global.update(license='').where(Global.user_id == message.text).execute()
                self.send(message.from_user.id, f'[✅]Вы успешно забрали лицензию у пользователя {message.text}', reply_markup=keyboard.adminPanel)
            else:
                self.send(message.from_user.id, '[🚫]Повторите команду! Id пользователя состоит из цифр', reply_markup=keyboard.adminPanel)
        elif message.text == '💢Отмена💢':
            self.send(message.from_user.id, '[❗]Действие отменено', reply_markup=keyboard.adminPanel)
        else:
            self.send(message.from_user.id, '[🚫]Пользователя не существует', reply_markup=keyboard.adminPanel)

    def startSpam(self, message):
        userInfo = Global.select().where(Global.user_id == message.from_user.id)
        text = message.text.split(' ')
        if text[0][0] == '7':
            if len(text) > 1 and text[1].isdigit():
                if int(text[1]) < 60:
                    if text[0].isdigit() and len(text[0]) == 11:
                        if text[0] not in self.attack:
                            if not WhiteNumber.select().where(WhiteNumber.number == text[0]).exists():
                                x = Thread(target=self.startingSpam, args=(message.from_user.id, text[0], text[1]))
                                print(x)
                                print(f'Запущен спам на номер {text[0]} от пользователя {message.from_user.id}')
                            else:
                                self.send(message.from_user.id, '[🚫]Этот номер в белом листе!', reply_markup=keyboard.startSpam)
                        else:
                            self.send(message.from_user.id, '[❗]Этот номер уже атакуют', reply_markup=keyboard.startSpam)
                    else:
                        self.send(message.from_user.id, '[🚫]Не правильный номер', reply_markup=keyboard.startSpam)
                else:
                    self.send(message.from_user.id, '[❗]Нельзя указывать больше 60 циклов',
                              reply_markup=keyboard.startSpam)
            else:
                self.send(message.from_user.id, '[🚫]Не правильно выполнен запрос', reply_markup=keyboard.startSpam)
        elif message.text == '❌Выйти❌':
            if userInfo[0].adm:
                self.send(message.from_user.id, '[❗]Вы вышли в основное меню', reply_markup=keyboard.userPanelAdm)
            else:
                self.send(message.from_user.id, '[❗]Вы вышли в основное меню', reply_markup=keyboard.userPanel)
        else:
            self.send(message.from_user.id, '[🚫]Номер должен начинаться с 7. Повторите команду', reply_markup=keyboard.startSpam)

    def startingSpam(self, user_id, number, count):
        self.attack.append(user_id)
        self.send(user_id, '[✅]Спам успешно запущен!', reply_markup=keyboard.startSpam)
        for i in range(int(count)):
            Spam(number)
            time.sleep(2)
        self.attack.remove(user_id)
        self.send(user_id, f'Спам на номер {number} успешно завершен')


Telegs(token, admin_id)
