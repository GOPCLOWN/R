import telebot

userPanel = telebot.types.ReplyKeyboardMarkup(True, False)
userPanel.add('🔥Начать спам', '💡Белый лист')
userPanel.add('😎Подписки', '🙎Профиль')
userPanel.add('👌SmS со своим текстом', '👑Деанон')
userPanel.add('🚨Помощь', '💸Статистика')

startSpam = telebot.types.ReplyKeyboardMarkup(True, False)
startSpam.add('💌SmS', '📞Call')
startSpam.add('❌Выйти❌')

userPanelAdm = telebot.types.ReplyKeyboardMarkup(True, False)
userPanelAdm.add('🔥Начать спам', '💡Белый лист')
userPanelAdm.add('😎Подписки', '🙎Профиль')
userPanelAdm.add('👌SmS со своим текстом', '👑Деанон')
userPanelAdm.add('🚨Помощь', '💸Статистика')
userPanelAdm.add('🥇Админ-панель🥇')

whiteList = telebot.types.ReplyKeyboardMarkup(True, False)
whiteList.add('🔒Добавить', '🔓Удалить')
whiteList.add('❌Выйти❌')

adminPanel = telebot.types.ReplyKeyboardMarkup(True, False)
adminPanel.add('Выдать лицензию', 'Забрать лицензию')
adminPanel.add('Выдать баланс', 'Забрать баланс')
adminPanel.add('Сервер', 'Статистика')
adminPanel.add('Обновить прокси')
adminPanel.add('Назад')

cancelButton = telebot.types.ReplyKeyboardMarkup(True, False)
cancelButton.add('💢Отмена💢')

cancelButton2 = telebot.types.ReplyKeyboardMarkup(True, False)
cancelButton2.add('❌Выйти❌')

subscription = telebot.types.InlineKeyboardMarkup(row_width=1)
day1 = telebot.types.InlineKeyboardButton(text='1 день | 10 рублей', callback_data='1d')
day7 = telebot.types.InlineKeyboardButton(text='7 дней | 50 рублей', callback_data='7d')
day14 = telebot.types.InlineKeyboardButton(text='14 дней | 100 рублей', callback_data='14d')
day30 = telebot.types.InlineKeyboardButton(text='30 дней | 150 рублей', callback_data='30d')
allDay = telebot.types.InlineKeyboardButton(text='Навсегда | 300 рублей', callback_data='always')
subscription.add(day1, day7, day14, day30, allDay)