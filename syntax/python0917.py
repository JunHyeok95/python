# print("Hello world")


# print('hello')
# num1 = 10
# num2 = 20
# print(num1+num2)


# str = input()
# int = int(input())
# float = float(input())
# print(str, int, float)


# name = input()
# print('hello',name)


# name = "name"
# age = 15
# age2 = 20
# age3 = age + age2
# print("Hello")
# print("hello"+ name)
# print("age", age)


# list = []
# list2 = [1, 2, 3, True, False]
# list3 = [(7, 8, 9), {"name":"user"}, [4, 5, 6]]
# list4 = [list, list2]
# print(list, list2)
# print("----------------")
# print(list3)
# print("----------------")
# print(list4)
# print("----------------")
# print(len(list),len(list2),len(list3),len(list4))


# list=[0, 1, 2, 3, 4, 5]
# print(list.index(2))
# list.insert(3, -1)  # 3번쨰에 -1을 추가
# print(list)
# list.append(50)
# print(list)
# list.extend([10,20])
# print(list)
# list.sort()
# print(list)
# list.reverse()
# print(list)


# mylist = [1, 2, 3, 4, 5]
# mylist.insert(0, 6)
# mylist.insert(len(mylist), 0)
# print(mylist)
# mylist.reverse()    # 리버스
# print(mylist)


# list = [1,2,3,4,5]
# del list[3] # 인덱스 3을 찾아서 삭제
# print(list)
# list.remove(2)  # 벨류 2를 찾아서 삭제
# print(list)
# del list[list.index(5)] # 5를 찾아서 인덱스로 삭제
# print(list)


# list = [1,2,3,4,5]
# print('삭제 할 숫자를 입력하장')
# value = int(input())
# list.remove(value)
# print(list)


# list = [0,1,2,3,4,5,6,7,8,9]
# print(list[0], list[-1]) # -1은 마지막 숫자입니당


# rect = (10, 20, 100, 150)
# rect2 = 20, 30, 40, 50
# print(type(rect), type(rect2))
# print(rect)
# print(rect[2])
# print(rect2)
# rect =(10, 20)
# print(rect)


# first = "Hello 'friend' "
# second = 'Hello "friend" '
# third = """
# Hello
# friend
# """
# fourth = '''
# hello~!
# friend~!
# '''
# print(first, second)
# print(third)
# print(fourth)


# str = 'Hello everyone'
# arr = str.split()
# print(arr)
# arr2 = list(str)
# print(arr2)
# str2 = ':'.join(arr2)
# print(str2)
# str3 = ''.join(arr2)
# print(str3)


# list=[0,1,2,3,4,5,6,7,8,9]
# print(list[5:8])
# print(list[7:])
# print(list[:4])
# print(list[::3])


# list=[0,1,2,3,4,5,6,7,8,9]
# print(list[::-1])


# capitals={'Korea':'Seoul', 'UK':'London'}   # 딕셔너리를 연습합니다
# days = {1:31, 2:28, 3:31, 4:30}
# print(capitals)
# print(days[3])
# days[5] = 31    # 항목 추가
# print(days)
# del capitals['UK']  # 항목 삭제
# print(capitals)
# capitals.update({'USA':'Wash','China':'Beijing'})
# print(capitals)


# set1 = set([1,2,3,1.1,2,2.3,3, 'hello'])
# set2 = {(1,2),3,4,5, 'hello'}
# print(set1,'허허')
# print(set2)
# print(set1 & set2)
# print(set1.intersection(set2))
# print(set1 | set2)
# print(set1-set2)
# set1.remove('hello')


# a = 20
# b = 30
# c = 6
# d = 2
# print(c ** d)
# print(a // c)


# a1 = True
# b1 = False
# c1 = True
# print(a1 and b1)
# print(c1 and b1)
# print(a or b)
# print(not a)


# var = int(input())
# if var > -1:
#     print('OK')
# else:
#     print('NG')


# password = input()
# if len(password) >= 8:
#     print('ok')
# else:
#     print('nono')


# num1 = int(input())
# num2 = int(input())
# if num1 > 0 and num2 > 0:
#     print('ok')
# elif num1 < 0 and num2 < 0 :
#     print('no')
# else:
#     print('soso')


# num = int(input())
# if num % 2 > 0:
#     print('even')
# else:
#     print('odd')


# print('나이를 입력하세요')
# age = int(input())
# if age > 19:
#     print('adult')
# elif 19 >= age > 12:
#     print('teenager')
# else:
#     print('kid')


# print('pass input')
# pass1 = int(input())
# if 4 <= pass1 <= 10:
#     print('ok')
# else:
#     print('NG')


# age = 18
# print('Hello') if age > 19 else print ('Too young')
# print('gogo' if age > 19 else 'nono')


# num1 = int(input())
# num2 = int(input())
# print( 'OK' if num1 + num2 >= 0 else 'NG' )


# print('num1 input')
# num1 = int(input())
# print('num2 input')
# num2 = int(input())
# print('op input + or -')
# op = input()
# print('result')
# print(num1+num2 if op=='+' else num1-num2 )


# arr = [1,2,3,4,5,6,7,8,9]
# for i in arr:
#     if i % 2 > 0:
#         print(i)
# # for i in arr[::2]:
# #     print(i)


# even = 0
# odd = 0
# arr = [1,2,3,4,5,6,7,8,9]
# for i in arr:
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print('even = ',even , 'odd = ',odd)


# # 딕셔너리를 연습합니다
# capitals={'Kkorea':'Seoul', 'UK':'London'}
# days = {1:31, 2:28, 3:31, 4:30}
# print(capitals)
# print(days[3])
# days[5] = 31 # 항목 추가
# print(days)
# del capitals['UK']
# print(capitals)
# capitals.update({'USA':'Wash','China':'Beijing'})
# print(capitals)


# set1 = set([1,2,3,1.1,2,2.3,3, 'hello'])
# set2 = {(1,2),3,4,5, 'hello'}
# print(set1,'허허')
# print(set2)
# print(set1 & set2)
# print(set1.intersection(set2))
# print(set1 | set2)
# print(set1-set2)
# set1.remove('hello')


# a = 20
# b = 30
# c = 6
# d = 2
# print(c ** d)   # 제곱 구하기
# print(a // c)   # 몫 구하기


# a1 = True
# b1 = False
# c1 = True
# print(a1 and b1)
# print(c1 and b1)
# print(a or b)
# print(not a)


# var = int(input())
# if var > -1:
#     print('OK')
# else:
#     print('NG')


# password = input()
# if len(password) >= 8:
#     print('ok')
# else:
#     print('nono')


# num1 = int(input())
# num2 = int(input())
# if num1 > 0 and num2 > 0:
#     print('ok')
# elif num1 < 0 and num2 < 0 :
#     print('no')
# else:
#     print('soso')


# num = int(input())
# if num % 2 > 0:
#     print('even')
# else:
#     print('odd')


# print('나이를 입력하세요')
# age = int(input())
# if age > 19:
#     print('adult')
# elif 19 >= age > 12:
#     print('teenager')
# else:
#     print('kid')


# print('pass input')
# pass1 = int(input())
# if 4 <= pass1 <= 10:
#     print('ok')
# else:
#     print('NG')


# age = 18
# print('Hello') if age > 19 else print ('Too young')
# print('gogo' if age > 19 else 'nono')


# num1 = int(input())
# num2 = int(input())
# print( 'OK' if num1 + num2 >= 0 else 'NG' )


# print('num1 input')
# num1 = int(input())
# print('num2 input')
# num2 = int(input())
# print('op input + or -')
# op = input()
# print('result')
# print(num1+num2 if op=='+' else num1-num2 )


# arr = [1,2,3,4,5,6,7,8,9]
# for i in arr:
#     if i % 2 > 0:
#         print(i)
# # for i in arr[::2]:
# #     print(i)


# even = 0
# odd = 0
# arr = [1,2,3,4,5,6,7,8,9]
# for i in arr:
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print('even = ',even , 'odd = ',odd)