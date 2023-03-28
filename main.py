#15 МОДУЛЬ
import json

import telebot

# два вида файла
# текстовые (.txt, .html) и бинарные (изображенияб аудио, видео)

# Путь к файлу абсолютный (С://) и относительный.

# r (read)
# w (write)
# a (append) dlya dozapisi
# b (binary)

# myfile = open ('hello.txt', 'w')
# myfile.close()

# with open('hello2.txt', 'w') as somefile:
#     somefile.write('goodbye world')
#
# with open('test1.txt', 'a') as file:
#     file.write('\nBye')
#
# data = {
#     "name": "Liliya",
#     "age": 25
# }
# with open("data_file.json", "w") as f:
#     json.dump(data, f)



# 16 МОДУЛЬ
# class Parrot:
#     species = 'птица'
#     def __init__(self, name, age):
#        self.name = name
#        self.age = age
# # создаем экземпляр класса
# kesha = Parrot('Кеша', 18)
# cookie = Parrot('Куки', 15)
# # получаем доступ к атрибутам класса
# print(f'Кеша - {kesha.__class__.species}')
# print(f'Куки тоже - {cookie.__class__.species}')
# # получаем доступ к атрибутам экземпляра
# print(f'{kesha.name}-{kesha.age} летний попугай')
# print(f'{cookie.name}, {cookie.age} летний попугай')

# методы
# class Parrot:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sing(self, song):
#         return f'{self.name} поет {song}'
#     def dance(self, dance):
#         return f'{self.name} танцует {dance}'
# kesha = Parrot('Кеша', 18)
# print(kesha.sing('песенки'))
# print(kesha.dance('шарманку'))

#Наследование
#родительский класс
# class Bird:
#     def __init__(self):
#         print('The bird is ready')
#     def WhoisThis(self):
#         print('Bird')
#     def swim(self):
#         print('swim faster')
#Дочерний класс
# class Penguin(Bird):
#     def __init__(self):
#         super().__init__()
#         print('Pinguin is ready')
#     def WhoisThis(self):
#         print('Pinguin')
#     def run(self):
#         print('Run faster than bird')
# peggy = Penguin()
# peggy.WhoisThis()
# peggy.swim()
# peggy.run()

#Инкапсуляция
# _ __
# class Computer:
#     def __init__(self):
#         self.__maxprice = 900
#     def sell(self):
#         print(f'price for sell {self.__maxprice}')
#     def setMaxPrice(self, price):
#         self.__maxprice = price
# c = Computer()
# c.sell()
# #change price
# c.__maxprice = 1000
# c.sell()
# # use function to change the price
# c.setMaxPrice(1000)
# c.sell()

#polimorfizm
#can use one (the same) function for different data
# class Parrot:
#     def fly(self):
#         print('the Parrot can fly')
#     def swim(self):
#         print('the Parrot can not swim')
# class Penguin:
#     def fly(self):
#         print('the Pinguin can not fly')
#     def swim(self):
#         print('the Pinguin can swim')
# def flying_test(bird):
#     bird.fly()
# kesha = Parrot()
# peggy = Penguin()
# #passing objects as arguments
# flying_test(kesha)
# flying_test(peggy)

#n- number of sides
# sides - list, it contains the dimentions of the sides
# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
# #takes the dimentions of the each side
#     def inputSides(self):
#         self.sides = [float(input('add side' + str(i+1)+ ':')) for i in range(self.n)]
# #displays on screen
#     def dispSides(self):
#         for i in range(self.n):
#             print('side', i+1, ' - ', self.sides[i])
# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self, 3)
#     def findArea(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)**0.5)
#         print('area of triangle', area)
# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()

# Data Modul 17
# Module 18
# import requests
#
# r = requests.get(
#     'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
# print(r.content)

# import requests
#
# r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# print(r.status_code)  # узнаем статус полученного ответа
# import requests
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json ответ
# print(r.content)
# import requests
# import json  # импортируем необходимую библиотеку
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
# print(type(texts))  # проверяем тип сконвертированных данных
#
# for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
#     print(text[:50], '\n')
# import requests
# import json
#
# r = requests.get('https://api.github.com')
#
# d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
#
# print(type(d))
# print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений
#
# import requests
#
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем пост запрос
# print(r.content)  # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет

# import requests
# import json
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
#
# r = json.loads(r.content)
#
# print(r[0])

# import telebot
#
# TOKEN = "6281415242:AAGlnpMnQjj_R1soaqzAFAmzve3bg9PrswM"
# bot = telebot.TeleBot(TOKEN)
# @bot.message_handler(commands=['start'])
# def function_name(message):
#     bot.reply_to(message, "Выберете команду из меню")
# bot.polling(none_stop=True)

# pip3 install lxml
#
# import telebot
# TOKEN = '6103608646:AAEjprAnWIOP34S-URqqmD0zxEW3DzolaYc'
# bot = telebot.TeleBot(TOKEN)
# keys = {
#     'биткоин': "BTC",
#     'эфириум': 'ETH',
#     "доллар": 'USD',
# }
# @bot.message_handler(commands=['start', 'command1'])
# def help(message: telebot.types.Message):
#     text = 'Чтобы начать работу введите комманду боту в следующем формате:\n<имя валюты> \
# < в какую валюту перевести> \
# <колличество переводимой валюты>\nУвидеть список всех доступных валют: /values'
#     bot.reply_to(message, text)
#
# @bot.message_handler(commands=['values', 'command2'])
# def values(message: telebot.types.Message):
#     text = "Доступные валюты:"
#     for key in keys.keys():
#       text = '\n'.join((text, key,))
#     bot.reply_to(message, text)
#
# @bot.message_handler(content_types=['text',])
# def convert(message: telebot.types.Message):
#     quote, base, amount = message.text.split(" ")
#     r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
#     text = json.loads(r.conetnt)[keys[base]]
#     bot.send_message(message.chat.id, text)
# bot.polling()

#функция сортировки методом 'пузырек'
def sort_puzirek(numbers_list_mod):
    for i in range(len(numbers_list_mod)):
        for j in range(len(numbers_list_mod) - i - 1):
            if numbers_list_mod[j] > numbers_list_mod[j + 1]:
                numbers_list_mod[j], numbers_list_mod[j + 1] = numbers_list_mod[j + 1], numbers_list_mod[j]
    return numbers_list_mod
#функция 'бинарного' поиска левого и правого элементов
def binary_search(numbers_list_mod, numbers_user, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if numbers_list_mod[middle] == numbers_user:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif numbers_user < numbers_list_mod[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(numbers_list_mod, numbers_user, left, middle - 1)
    else:  # иначе в правой
        return binary_search(numbers_list_mod, numbers_user, middle + 1, right)
# тело программы
#вводим числа, проверяем правильность данных, сортируем
what = True
while what:
    try:
        numbers_list = input("Введите последовательность натуральных чисел через пробел: ").split()
    #    print('введено:', numbers_list)

    # разделяем по разделителю (пробел) и записываем строку целых чисел
        numbers_list_mod = [int(x) for x in numbers_list]
    #    print('числа:', numbers_list_mod)
    # сортировка
        numbers_list_mod = sort_puzirek(numbers_list_mod)
        print('после сортировки методом пузырек:', numbers_list_mod)

        numbers_user = input("Введите число для определения индекса: ")
        numbers_user = int(numbers_user)
    #    print("введено число ", numbers_user)
        what = False
    except ValueError:
            print(f'Ошибка {ValueError}')
            print('Введено недопустимое значение.')
            what = input("Повторить ввод чисел? (+ или -): ")
            if what != '+':
                print('До свидания')
                what = False
                exit(1)
            else:
                print('В следующий раз будьте внимательнее!')

#проверяем есть ли искомое число в списке
if numbers_user not in numbers_list_mod:
     print(f'Нет числа {numbers_user} среди чисел последовательности. {numbers_list_mod}')
     if numbers_user < min(numbers_list_mod):
           print(f'число {numbers_user} меньше минимального последовательности. {min(numbers_list_mod)}')
     if numbers_user > max(numbers_list_mod):
           print(f'число {numbers_user} больше максимального последовательности {max(numbers_list_mod)}')
     exit(1)

#вызывается функция бинарного поиска левого и правого элементов
number_index = binary_search(numbers_list_mod, numbers_user, 0, len(numbers_list_mod) - 1)

#определяем место искомого числа в списке
print("Индекс введенного числа в списке (от 0): ", number_index)
#анализ числа в списке
if number_index == 0:
    print(f'число {numbers_user} первое значение в списке, следующее {numbers_list_mod[number_index + 1]}')
elif number_index == int(len(numbers_list_mod)-1):
    print(f'число {numbers_user} последнее значение в списке, предыдущее значение {numbers_list_mod[number_index-1]}')
else:
    print(f'предыдущее значение {numbers_list_mod[number_index-1]}, следующее {numbers_list_mod[number_index + 1]}')
















