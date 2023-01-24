# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.

def set_phrase_list():
    data = open('phrase.txt', mode= 'r', encoding= 'utf - 8')
    phrase_list = data.readlines()
    data.close()
    dictionary = {}
    for phrase in phrase_list:
        phrase = phrase.removesuffix('\n')
        phrase = phrase.split(': ')
        dictionary[phrase[0]] = phrase[1]
    return dictionary

bot_script = set_phrase_list()

# # МОЙ ВАРИАНТ
# user_text = input('Задайте вопрос чат-боту: ')

# if user_text in bot_script:
#     print(bot_script[user_text])
# else:
#     print('Я не понимаю')

# ДРУГОЙ ВАРИАНТ

start_dialog = True

while start_dialog:
    phrase = input('Я: ')
    phrase = phrase.lower()
    if phrase in bot_script.keys():
        print(f'Бот: {bot_script[phrase]}')
    else:
        print(f'я не понимаю')
        check = input('Бот: скажешь мне правильный ответ (Y/N)?\nЯ: ')
        check = check.lower()
        if check == 'y':
            answer = input(f'Бот: как ты ответишь на "{phrase}"?\nЯ: ')
            data = open('phrase.txt', mode= 'a', encoding= 'utf-8')
            data.write(f'{phrase}: {answer}\n')
            data.close()
            bot_script[phrase] = answer
            # bot_script = set_phrase_list()
    if phrase == 'выход':
        start_dialog = False
