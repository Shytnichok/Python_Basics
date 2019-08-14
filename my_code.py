
print('Friender: Симулятор воображаемого друга')

# Необходимые константы
phrases_about_age = [
    ' - Скажи просто м (мужского) или ж (женского)\n - ',
    ' - Так трудно сказать какого ты пола?\n - ',
    ' - Это же не сложно. М или Ж? \n - ',
    ' - Может хватит дурачиться?\n - ',
    ' - Ну скажи!\n - '
]
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
robot_answer = ''

user_info = {
    'name': input(' - Как тебя зовут?\n - '),
    'age': 0,
    'sex': '',
    'pet_name': '',
    'gamer': 0,
}

answer = input(' - Сколько тебе лет?\n - ')
while not answer.isdigit():
    answer = input(' - Сколько тебе лет?\n - ')
user_info['age'] = int(answer)

sex = input(' - Какого ты пола? (М/Ж)\n - ')
while sex.lower() != 'м' and sex.lower() != 'ж':

    for phrase in phrases_about_age:
        sex = input(phrase)

        if sex.lower() == 'м' or sex.lower() == 'ж':
            user_info['sex'] = sex.upper()
            break;

    if sex.lower() == 'м' or sex.lower() == 'ж':
        user_info['sex'] = sex.upper()
        break;

user_info['pet_name'] = input(' - Как зовут твоего питомца?\n - ')

answer = input(' - Любишь играть? (Да/Нет)\n - ')
while answer.lower() != 'да' and answer.lower() != 'нет':
    answer = input(' - Любишь играть? (Да/Нет)\n - ')
user_info['gamer'] = answer.lower() == 'да'

if user_info['age'] < 18:
    print(' - Ты слишком молод. Мама отругает.')

elif user_info['age'] > 90:
    print(' - ' + user_info['name'] + ', для вас в таком возрасте это может быть утомительно!')
    answer = input('   Вы уверены, что хотите сыграть в игру? (Да/Нет)\n - ')

    if answer == 'Да':
        answer = input(' - Вы точно уверены, что хотите сыграть в игру? (Да/Нет)\n - ')

        if answer == 'Да':
            print(' - Хорошо. Начнем игру!')

        elif answer == 'Нет':
            print(' - На нет и суда нет. Всего хорошего, '+ user_info['name'] + '!')

        else: #Дал ответ ни Да ни Нет
            pass;
    elif answer == 'Нет':
        print(' - На нет и суда нет. Всего хорошего, ' + user_info['name'] + '!')

    else :#Дал ответ ни Да ни Нет
        pass
      
else:
    print(' - Рад тебя видеть, '+ user_info['name'] + '! Давай назову буквы алфавита, которых нет в твоем имени:')
    for char_alphabet in alphabet:
        #for char_name in user_info['name']
        if (user_info['name'].upper()).find(char_alphabet) + 1:
            robot_answer += '_'
            continue
        robot_answer += char_alphabet
    print('   ',robot_answer)
    print('   Это все, чему я научился. Подожди немного и увидишь как я вырасту!')
    
    
