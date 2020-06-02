"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import locale
locale.setlocale(locale.LC_ALL, "russian")
from datetime import datetime, date, timedelta

def print_days():
    d_today = date.today()
    print(d_today.strftime('%d.%m.%Y'))

    delta = timedelta(days=1)
    d_yesterday = d_today - delta
    print(d_yesterday.strftime('%d.%m.%Y'))

    delta = timedelta(days=30)
    month_ago = d_today - delta
    print(month_ago.strftime('%d.%m.%Y'))


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_string = '01/01/20 12:10:03.234567'
    date_dt = datetime.strptime(date_string, '%y/%m/%d %H:%M:%S.%f')
    print(date_dt)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))