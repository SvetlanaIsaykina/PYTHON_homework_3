# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.

bot_script = {
    'привет': 'Добрый день!',
    'как тебя зовут': 'Меня зовут Алина',
    'кто ты': 'Я твой помощник',
    'чем ты можешь мне помочь': 'Объясню основы PYTHON',

}

user_text = input('Задайте вопрос чат-боту: ')

if user_text in bot_script:
    print(bot_script[user_text])
else:
    print('Я не понимаю')
