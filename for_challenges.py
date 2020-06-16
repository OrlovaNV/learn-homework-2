from operator import index

names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in names:
    print(i)

    print(len(i))

is_male ={
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for i in names:
    if is_male[i] == False:
        print(f'{i} - пол женский.')
    else:
        print(f'{i} - пол мужской.')

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print(f'Всего {len(groups)} группы.')
number_group = 0
for group in groups:
    number_group += 1
    print(f'В группе {number_group} - {len(group)} ученика')
    a = ', '
    print(f'Группа {number_group}: {a.join(group)}')

