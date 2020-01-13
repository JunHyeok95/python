# class Circle: # 연산자 오버라이딩
#     def __init__(self, x=0, y=0, r=1):
#         self.x=x
#         self.y=y
#         self.r=r
#     def __del__(self):
#         print('delete')
#     def __repr__(self):
#         return 'circle'
#     def __add__(self, other):
#         return self.x+other.x, self.y+other.y
#     def __sub__ (self, other):
#         return self.x-other.x, self.y-other.y
#     def __eq__(self, other):
#         if self.r == other.r and self.x == other.x and self.y == other.y:
#             return True
#         else:
#             return False
# c1 = Circle()
# c2 = Circle(0, 0, 2)
# print(c1, c2)


# class Member: # 상속
#     def __init__(self):
#         self.memberid = '0'
#     def __repr(self):
#         return 'memeber id = '+self.memberid
# class Student(Member):
#     pass
# s = Student()
# print(s)


# class Member: # 상속과 super() 생성
#     def __init__(self):
#         self.memberid = '0'
#     def __repr(self):
#         return 'memeber id = '+self.memberid
# class Student(Member):
#     def __init__(self, major = 'computer'):
#         super().__init__()
#         self.major = major
# s = Student()
# print(s.memberid)


# class Member:   # 오버라이딩
#     def __init__(self):
#         self.memberid = '0'
#     def __repr__(self):
#         return 'memeber id = '+self.memberid
# class Student(Member):
#     def __init__(self, major = 'computer'):
#         super().__init__()
#         self.major = major
#     def __repr__(self):
#         return 'memeber id = '+self.major
# s = Student()
# print(s)


# class Member:   # 부모 함수 오버라이딩
#     def __init__(self):
#         self.memberid = '0'
#     def __repr__(self):
#         return 'memeber id = '+self.memberid
# class Student(Member):
#     def __init__(self, major = 'computer'):
#         super().__init__()
#         self.major = major
#     def __repr__(self):
#         return super().__repr__() + ', major =' + self.major
# s = Student()
# print(s)


# file = open("file.txt", "w")
# file.write("Hello World\n")
# file.close()


# file = open("file.txt", "a")
# file.write("every one\n")
# file.close()


# import sys
# print(sys.argv)
# print("len = " , len(sys.argv))
# sys.stdout.write('hello\n')
# sys.stderr.write('error\n')


# import os
# print(os.name)
# print(os.getcwd()) # get Current Working Directory
# os.system('') # 흑.. 없다


# import math
# import random
# import statistics as st
# print('log', math.log(8, 2))
# print('pi', math.pi)
# print('sample', random.sample(range(100), 10))
# print('rand float', random.random())
# print('rand int', random.randint(10, 100))
# data = [i for i in range(1, 11)]
# data.append(100)
# print(data)
# print('choice', random.choice(data))
# print('mean', st.mean(data))
# print('median', st.median(data))
# print('variance', st.variance(data))
# print('stdev', st.stdev(data))


# import user
# print(user.hello())
# print(user.defaultUser.hello())
# myUser = user.User()
# print(myUser.hello(user.defaultName))
# user._merge('a', 'b')
# user.__merge('a', 'b')
# user._value
# user.__value


# from user import *
# print(hello())
# print(defaultUser.hello())
# myUser = User()
# print(myUser.hello(defaultName))
# _merge('a', 'b')
# _value


# import module
# print(module.func())