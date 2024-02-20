import telebot
import prived_info

@prived_info.bot.message_handler(commands=['start'])

def hello(info):
    user_name = info.from_user.username
    prived_info.bot.send_message(info.chat.id, f'hello {user_name}')
    prived_info.bot.send_message(info.chat.id, info.from_user.id)



prived_info.bot.polling(none_stop=True)