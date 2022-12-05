from schedule import Schedule
from telebot import types


def getSchedText(dayNumber: int) -> str:
    return f'День недели: <b>{Schedule.getDayName(dayNumber)}</b>'


def getSchedBtns(dayNum: int) -> types.InlineKeyboardMarkup:
    btns = types.InlineKeyboardMarkup(row_width=2)
    sched: dict = Schedule().getSchedule()
    for lessionNum in sched[dayNum]:
        btnLesson = types.InlineKeyboardButton(text=f' {sched[dayNum][lessionNum]}', callback_data="backToMenu")
        btnTime = types.InlineKeyboardButton(text=f'{Schedule.getTime(lessionNum)}', callback_data="backToMenu")
        btns.add(btnTime, btnLesson)
    btns.add(types.InlineKeyboardButton(text=f'Назад в меню', callback_data=f'mainmenu'))
    return btns


def getWeekBtns() -> types.InlineKeyboardMarkup:
    btns = types.InlineKeyboardMarkup(row_width=3)
    for i in range(0, 5):
        btnDay = types.InlineKeyboardButton(text=f'{Schedule.getDayName(i)}', callback_data=f'weekDay|{i}')
        btnTime = types.InlineKeyboardButton(
            text=f'{getLastLesson(i)} уроков - {getLastLessonTime(i)}', callback_data=f'weekDay|{i}'
        )
        btns.add(btnDay, btnTime)
    btns.add(types.InlineKeyboardButton(text=f'Назад в меню', callback_data=f'mainmenu'))
    return btns


def getMainmenuBtns() -> types.InlineKeyboardMarkup:
    btns = types.InlineKeyboardMarkup(row_width=1)
    btnToday = types.InlineKeyboardButton(text='Расписание на сегодня', callback_data="today")
    btnTmrrw = types.InlineKeyboardButton(text='Расписание на завтра', callback_data="tmrrw")
    btnWeek = types.InlineKeyboardButton(text='Выбрать день', callback_data="week")
    btns.add(btnToday, btnTmrrw, btnWeek)
    return btns


def getLastLessonTime(dayNum: int) -> str:
    lastLesson: int = getLastLesson(dayNum) - 1
    return Schedule.getTime(lastLesson).split(' - ')[1]


def getLastLesson(dayNum: int) -> int:
    return list(Schedule().getSchedule()[dayNum])[-1] + 1
