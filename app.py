from config import bot, chips
from datetime import datetime as dt
from helpers import getWeekBtns, getSchedText, getSchedBtns, getMainmenuBtns


@bot.message_handler(content_types=['text'])
def deleteMsgText(msg):
    bot.delete_message(msg.chat.id, msg.message_id)
    match msg.text:
        case '/start': return mainmenu(msg)
        case '/today': return today(msg)
        case '/tmrrw': return tmrrw(msg)
        case '/week': return week(msg)


def mainmenu(msg):
    btns = getMainmenuBtns()
    text = 'Добро пожаловать в расписание <a href="https://www.twitch.tv/sufferfrd">Suffer</a>'
    bot.send_photo(msg.chat.id, photo=chips, caption=text, reply_markup=btns, parse_mode='html')


def today(msg):
    thisday = dt.now().weekday()
    sendSchedule(msg, thisday)


def tmrrw(msg):
    tmrrwday = dt.now().weekday() + 1
    sendSchedule(msg, tmrrwday)


@bot.message_handler(commands=['week'])
def week(msg):
    btns = getWeekBtns()
    bot.send_message(msg.chat.id, text='Расписание на неделю', reply_markup=btns)


def sendSchedule(msg, dayNum: int):
    btntext = getSchedText(dayNum)
    btns = getSchedBtns(dayNum)
    bot.send_message(msg.chat.id, text=btntext, reply_markup=btns, parse_mode='html')


def backToMenu(msg):
    return mainmenu(msg)


@bot.callback_query_handler(func=lambda call: True)
def inline_handler(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data.split('|')[0] == 'weekDay':
        sendSchedule(call.message, int(call.data.split('|')[1]))
    else:
        funcname = globals()[f'{call.data}']
        funcname(call.message)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
