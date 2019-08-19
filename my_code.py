game_name = 'Friender: Симулятор воображаемого друга'
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

print('Добро пожаловать в игру - {}'.format(game_name))

# Необходимые константы
phrases_about_age = [
    ' - Скажи просто м (мужского) или ж (женского)\n - ',
    ' - Так трудно сказать какого ты пола?\n - ',
    ' - Это же не сложно. М или Ж? \n - ',
    ' - Может хватит дурачиться?\n - ',
    ' - Ну скажи!\n - '
]
robot_answer = ''
temp = ''
user_info = {
    'name': {'question': 'Как тебя зовут?' ,'answer': None},
    'age': {'question': 'Сколько тебе лет?' ,'answer': 0},
    'sex': {'question': 'Какого ты пола? (М/Ж)' ,'answer': None},
    'pet_name': {'question': 'Как зовут твоего питомца?' ,'answer': None},
    'gamer': {'question': 'Любишь играть? (Да/Нет)','answer': None},
}
for itm in user_info:
    while temp != 'exit':
        temp = input(' - {}\n - '.format(user_info[itm]['question']))

        if itm == 'age':
            if temp.isdigit():
                user_info[itm]['answer'] = int(temp)
                break
            elif temp == 'exit':
                continue
            else:
                print(' * необходимо ввести число\n')
                continue
        temp = temp.lower()
        if itm == 'sex':
            if temp == 'м' or temp == 'ж':
                user_info[itm]['answer'] = temp
            elif temp == 'exit':
                continue
            else:
                print(' * необходимо ввести м или ж\n')
                continue
                '''
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
                '''

        elif itm == 'gamer':
            if temp == 'да':
                user_info[itm]['answer'] = True
            elif temp == 'нет':
                user_info[itm]['answer'] = False
            elif temp == 'exit':
                continue
            else:
                print(' * необходимо ввести ДА или НЕТ\n')
                continue
        else:
            user_info[itm]['answer'] = temp.title()
        break
    if temp == 'exit':
        break

# Start the Game

if user_info['age']['answer'] < 18 and temp != 'exit':
    print(' - Ты слишком молод. Мама отругает.\n')

elif user_info['age']['answer'] > 90 and temp != 'exit':
    print('{}, для вас в таком возрасте это может быть утомительно!'.format(user_info['name']['answer']))
    while True:
        answer = input('Вы уверены, что хотите сыграть в игру? (Да/Нет)\n - ').lower()

        if answer == 'да':
            answer = input(' - Вы точно уверены, что хотите сыграть в игру? (Да/Нет)\n - ').lower()
            if answer == 'да':
              print(' - Хорошо. Начнем игру!')

            elif answer == ' нет':
               print(' - На нет и суда нет. Всего хорошего, '+ user_info['name'] + '!')

            elif temp == 'exit': # Дал ответ ни Да ни Нет
                break
            else:
                pass
        elif answer == 'нет':
            print(' - На нет и суда нет. Всего хорошего, ' + user_info['name'] + '!')

        elif temp == 'exit':
            break
        else:
            pass

else:
    print(' - Рад тебя видеть, {}! Давай назову буквы алфавита, которых нет в твоем '
          'имени:'.format(user_info['name']['answer']))
    for char_alphabet in alphabet:
        if char_alphabet in user_info['name']['answer'].upper():
            robot_answer += '_'
            continue
        robot_answer += char_alphabet
    print('   ', robot_answer)
    print('   Это все, чему я научился. Подожди немного и увидишь как я вырасту!')

