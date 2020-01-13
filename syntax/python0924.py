# for i in range(1,10):
#     for j in range(1,10):
#         print(i*j, end=' ')
#     print()


# for i in range(0,3):
#     for j in range(i,3):
#         print('*', end='')
#     print()


# for index, value in enumerate([0, 2, 4, 6, 8, 10]):
#     print(index, value)


# arr = [ i for i in range(5,10) ]
# print("arr", arr)
# arr2 = [ i*2 for i in range(3) ]
# print("arr2", arr2)
# arr3 = [ i*3 for i in range(1,4)
#              for j in range(1,4) ]
# print("arr3", arr3)


# arr = [i for i in range(1, 11, 2)]
# print(arr)


# arr = [ i for i in range(10) if i%2==0 ]    # python 장점
# print(arr)
# scores = [ 80, 95, 66, 88, 70, 74, 98]
# a_grade = [ s for s in scores if s > 90 ]
# print(a_grade)


# set1 = {i for i in range(5)}    # 중복을 제거하는 Set comprehension
# print(set1)
# arr = [1, 1, 2, 2, 3, 3]
# set2 = {i for i in arr}
# print(set2)


# arr_id = ['학생1', '학생2', '학생3', '학생4', '학생5']
# arr_score = [80, 90, 90, 70, 80]
# dic = { key : value for key, value in zip(arr_id, arr_score)}
# print(dic)


# sum = 0
# value = -1
# arr = []
# while value != 0:
#     print("입력하장 >>> ", end = '')
#     value = int(input())
#     sum += value
#     if value > 0:
#         arr.append(value)
# print(sum)
# print(arr)


# sum = 0
# count = -1
# value = -1
# while value != 0:
#     print("입력하장 >>> ", end = '')
#     value = int(input())
#     sum += value
#     count += 1
# print("count = ",count,"avg = ",sum/count)


# sum = 0
# value = -1
# arr = []
# while value != 0:
#     print("입력하장 >>> ", end = '')
#     value = int(input())
#     arr.append(value)
# print(arr)


# arr = [1,1]
# print("피보나치 수열")
# print(arr, "을 이용하여서 배열을 만듭니다 !")
# print("원하는 값을 입력하장 >>> ", end='')
# value = int(input())
# for i in range(2, value+1):
#     arr.append(arr[i-1]+arr[i-2])
# print(arr)


# list = [123, 92, 87, 134, 112, 95, 78, 106, 109, 83]
# max = list[0]
# min = list[0]
# for i in list:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print("max = ", max, "min = ", min)


# list = [123, 92, 87, 134, 112, 95, 78, 106, 109, 83]
# max = list[0]
# min = list[0]
# maxIndex = 0
# minIndex = 0
# for i in range(1, len(list)):
#     if i > max:
#         max = list[i]
#         maxIndex = i
#     if i < min:
#         min = list[i]
#         minIndex = i
# print("max = ", max, "index = ", maxIndex)
# print("min = ", min, "index = ", minIndex)


# print("사용자로 부터 정수를 입력 받는다 >>> ", end='')
# list = input()
# for i in list[::]:
#     for j in range(0,int(i)):
#         print("*",end='')
#     print()
# """ 정답 """
# str = input()
# n = 0
# for i in str:
#     n = int(i)
#     for j in range(n):
#         print('*', end='')
#     print()


# a = 500     # 거스름 돈
# b = 100
# c = 50
# d = 10
# list = []
# print("물건 값 = ", end='')
# nedan = int(input())
# oturi = 1000 - nedan
# list.append(oturi//a)
# list.append(( oturi - list[0]*a ) //b)
# list.append(( oturi - list[0]*a - list[1]*b ) //c)
# list.append(( oturi - list[0]*a - list[1]*b - list[2]*c ) //d)
# print(list)


# price = int(input())
# list = [ 1000, 500, 100, 50, 10 ]
# cList = [ 0 for i in list ]
# change = 10000-price
# for i in range(0, len(list)):
#     while change >= list[i]:
#         change -= list[i]
#         cList[i] += 1
# for i, list2 in enumerate(list):
#     while change >= list2:
#         change -= list2
#         cList[i] += 1
# print(cList)


# import random       # "기본값을 실패로 두자"
# answer = random.randint(1, 100)
# cnt = 0
# print("숫자 마추기 게임 !!")
# while True:
#     cnt += 1
#     if cnt > 10:
#         print(" ### 패배 ### ")
#         print(" 정답은 ", answer)
#         break
#     print(">>> ", end='')
#     value = int(input())
#     if answer == value:
#         print(value, "정답 ~!")
#         break
#     elif answer > value:
#         print(value, "보다 크다")
#     elif answer < value:
#         print(value, "보다 작다")