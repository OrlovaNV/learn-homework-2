word = 'Архангельск'
print(f'Последняя буква в слове: {word[-1]}')

c = 0
for i in word.lower():
    if i == "а":
        c += 1
print(f'Количество букв "а" в слове: {c}')

Vowel = 0
x = ('а', 'е', 'и', 'о', 'у', 'ё', 'ю', 'я')
for i in word.lower():
    if i in x:
        Vowel += len(i)
print(f'Количество гласный букв в слове: {Vowel}')

sentence = 'Мы приехали в гости'
print(f'Количество слов в предложении: {len(sentence.split())}')

spisok = sentence.split(' ')
a = 0
for i in spisok:
    print(i[0])
    a += len(i)
    
average_wods =a/len(spisok)
print(average_wods)
    