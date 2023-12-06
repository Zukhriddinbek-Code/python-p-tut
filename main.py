# challenge calculate the volume of a right circular cone
# PI = 3.14
# r = 10
# h = 20
# volume = PI*(r*r)*h/3
# print(volume)

# challenge 2
# item1 = 10.99
# item2 = 5.95
# item3 = 8.49
# item4 = 2.75
# item5 = 12.99

# print("$", item1+item2+item3+item4+item5)

# review exercises for strings
# x = "hello world, \
#    this is multiline code \
#     displayed in single line"
# print(x)

# y = "this is a string that spans \n multiple lines, \n with whitespace preserved"
# print(y)


# x = 'hello'
# y = 'world'
# print(x + y)

# univ = 'sejong university'
# print(len(univ))

# str1 = 'Hello'
# str2 = 'World'
# print(str1 + str2)

# print(str1 + ' ' + str2)

# str_slice = 'bazinga'
# print(str_slice[2: -1])


# weight = 0.2
# animal = 'newt'

# print(weight, "kg in the wight of the new", animal)

# str = 'hello world, this is an example of counting words'
# words = len(str.split())
# chars = len(str)
# print(words, "words", chars, 'characters')

# t = (1, 2, [3, 4])
# print(t[2])
# b = 'python for Beginners'
# a = 'Python Essentials'
# # if a < b:
# #     print(a)
# # print(a < b)
# print('Python Essentials'.lower() == 'python for Beginners'.lower())

# is_first_login = True
# if is_first_login == True:
#     print("Welcome, new user!")
# else:
#     print("Welcome back!")

# text = "Python is great. Python is easy. Python is versatile."

# words = text.replace(".", "").lower().split()
# unique_words = set(words)
# print(unique_words)
# result = len(unique_words)
# # print(result)
# words = text.split()
# unique_words = set(words)
# print(unique_words)
# result = len(unique_words)

# email = 'zuhriddin@200'
# email_body = f"Dear {email}, We have a special offer for you!"
# print(email_body)

# t = ('hello question', ('france', 'madrid'))
# t[1] = 'trash'
# print(t[1])
# a = 10

# a += 20

# a = "10"
# print(type(a))
# a = 5
# b = 3
# s = 5 + 3
# d = 5 - 3
# result = (s, d)
# s, d = 5 + 3, 5 - 3,
# 3 + 5
# result = (d, s)
# print(type(result))
# s, d = 5 + 3, 5 - 3,
# 3 + 5
# print(s, d)

# age = input("Enter your age: ")
# age = int(input("Enter your age: "))
# print(age)
# message = "See you later!"

# preview = "..." + message[-4:]
# print(preview)

# def sum(a: int, b: int):
#     return a + b


# sum(1, 'e')
# from typing import Tuple


# def annotate_me(a: int, b: float, c: str) -> Tuple[float, str]:
#     return (a+b), str.upper(str)


# print(annotate_me(1, 2, 'hello'))

# import math

# print(dir(math))

# from example_data import emotions_data


# def main():
#     pass


# if __name__ == "main":

#     print(emotions_data.emotion_data_json)

# def valid_int(x: int):
#     if type(x) != int:
#         print('not int value')
#     else:
#         print(x)

# valid_int(1)
# import fire


# def hello(name='World'):
#     return 'Hello %s' % name


# if __name__ == '__main__':
#     fire.Fire(hello)

class Vehicle:
    def start():
        print('engine started')

    def move():
        print('engine is moving')

    def stop():
        print('engine stopped')


class Car(Vehicle):
    pass


class Truck(Vehicle):
    pass


class Train(Vehicle):
    pass
