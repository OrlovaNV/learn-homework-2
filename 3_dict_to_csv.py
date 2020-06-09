"""
Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
spisok = [
        {'name': 'Masha', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Vasya', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Misha', 'age': 48, 'job': 'Big boss'}, 
        {'name': 'Petya', 'age': 19, 'job': 'Student'}
    ]
 
with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in spisok:
        writer.writerow(user)

if __name__ == "__main__":
    main()
