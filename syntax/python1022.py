# num = 0
# try:
#     num = int(input())
# except ValueError:
#     num = 0
# finally:
#     print(num)


# list = [1, 2, 3]
# value = 0
# try:
#     index = int(input())
#     value = list[index]
# except (ValueError, IndexError):
#     value = list[0]
# print(value)


# num = int(input())
# try:
#     value = 10/num
# except ZeroDivisionError:
#     print('devision zero')
# else:
#     print(value)


# num = int(input())
# try:
#     value = 10/num
# except ZeroDivisionError as err:
#     print(err)
# else:
#     print(value)


# try:
#     num = int(input())
# except Exception as err:
#     print("input Err")      # 이 부분을 num 조작하면 else 가 한개 줄어든다.
#     exit()
#     print(err)
# else:
#     if 1 < num < 10: 
#         for i in range(1,10):
#             print(num,"*",i,"=",num*i)
#     else:
#         print("2~9 input")


# dict = {1:'one', 2:'two'}
# num1 = int(input())
# num2 = int(input())
# try:
#     value = 10/num1
#     value2 = dict[num2]
# except (ZeroDivisionError, KeyError):
#     print('error')
# else:
#     print(value, value2)


# dict = {1:'one', 2:'two'}
# num1 = int(input())
# num2 = int(input())
# try:
#     value = 10/num1
#     value2 = dict[num2]
# except ZeroDivisionError as error1:
#     print(error1)
# except KeyError as error2:
#     print(error2)
# else:
#     print(value, value2)


# def add(first, second):
#     if not type(first) is int or not type(second) is int:
#         raise TypeError
#     return first+second
# try:
#     add('1', 1)
# except TypeError:
#     print('not Not not Not')


# class MyClass:
#     def __init__(self, message):
#         print(message)
# value = MyClass('hello')


# class MyClass:
#     def __init__(self, message = 'hello'):
#         print(message)
# value = MyClass()
# value = MyClass('go')


# class MyClass:
#     def __init__(self):
#         pass
#     def say_hello(self):
#         print('hello world')
# my = MyClass()
# my.say_hello()


# class MyClass:
#     def __init__(self):
#         pass
#     def say_hello(self, message = 'hello'):
#         print('message',message)
# my = MyClass()
# my.say_hello()


# class MyClass:
#     def say_hello(self):
#         print('hello ~!')
# m = MyClass()
# MyClass.say_hello(m)


# class MyClass:
#     message = 'hello'
#     def __init__(self, name):
#         self.name = name
# print(id(MyClass.message))
# a = MyClass('a')
# print(a.name, id(a.name), a.message, id(a.message))
# b = MyClass('b')
# print(b.name, id(b.name), b.message, id(b.message))
# MyClass.message = 'bye'
# print(a.message, b.message)


# class MyClass:
#     str = 'hello'
# a = MyClass()
# b = MyClass()
# MyClass.str = 'bye'
# print(a.str, b.str)
# a.str = 'a'
# print(id(MyClass.str), id(a.str), id(b.str))


