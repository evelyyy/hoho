from time import sleep
from filters import filters


menu = ''
for i in filters:
    menu += str(i) + ') ' + filters[i]['name'] + '\n'
menu += '0) Выход'
while True:
    print(menu)
    sleep(0.3)
    m = int(input('Ввод: '))
    while not m in (0, 1, 2, 3, 4, 5):
        m = int(input('Или я чё-то недопёр или ты клавишами ошибься :)\nВвод: '))
    sleep(0.2)
    if not m:
        print('\nСпасибо за ревьюшку :>')
        print('Выход')
        for _ in range(3):
            sleep(0.3)
            print('\r. ', end='')
            sleep(0.3)
            print('\r.. ', end='')
            sleep(0.3)
            print('\r... ', end='')


    print('\n' + filters[m]['description'])
    while True:
        sure = input('\nПрименить фильтр к тексту (Да | Нет)\nВвод: ')
        while sure.lower() not in ('да', 'нет'):
            sure = input('\nкак так, два слова ведь...\nПрименить фильтр к тексту (Да | Нет)\nВвод: ')
        if sure.lower() == 'да':
            sleep(0.5)
            print('\n', filters[m]['start'](text))
            sleep(1.5)
            break
        else:
            break
