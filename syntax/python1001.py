# arr = [1, 7, 3, 8, 5, 9]
# for i in arr:
#     for i in arr-1:
#         print(i)


# arr = [99,77,55,44,66,88,33,44,22,10,3,4,7,9,43] 
# print(arr)
# range
# for i in range(len(arr)-1):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i] , arr[j] = arr[j] , arr[i]
# print(arr)


# def say_hello():
#     print("hello")
# def say_bye():
#     print("bye")
# say_hello()
# say_bye()


# def say_hello2(name):
#     print("hello", name)
# def say_bye2(name):
#     print("bye", name)
# say_hello2('abc')
# say_hello2('def')
# say_bye2('ghi')


# def add(first, second):
#     print(first, '+', second, '=', first + second)
# add(second=1, first=2)


# def bigger(big, little):
#     if big > little:
#         print(big)
#     else:
#         print(little)
#     print(big if big > little else little)
# bigger(1, 2)


# def hello(age, name='jang'):  # 디폴트는 마지막에 넣자
#     print('hello', age, name)   # print('' , end = ' ') 이것도 같은 원리
# hello(25)
# hello(25,'jun hyeok')


# def sum_int(*t):
#     sum = 0
#     for i in t:
#         if type(i) is int:
#             # print(type(i))
#             # print(t[i])
#             # sum += t[i]
#             sum += i
#     print(sum)
# sum_int(1, 1, 1.0, 2, '3', True)


# def func(first, second):
#     print(first, second, type(first))
# param1 = [1, 2]
# param2 = (3, 4)
# func( *param1 )
# func( *param2 )
# func( *[5, 6] )
# func( ** {"first":1, "second":2} )


# def myFunc1(*list):
#     print(list)
#     sum, cnt, avg = 0, 0, 0
#     for i in list:
#         if type(i) is int:
#             sum += i
#             cnt += 1
#     avg = sum / cnt
#     print("avg =", avg, " sum =", sum, " cnt=", cnt)
# myFunc1(1,2,3,4,5)


# def myFunc2(*list):
#     print(list)
#     sum, cnt, avg = 0, 0, 0
#     for i in range(1, len(list)-1):
#             sum += list[i]
#             cnt += 1
#     avg = sum / cnt
#     print("avg =", avg, " sum =", sum, " cnt=", cnt)
# myFunc2(1,4,5,6,2)


# def myFunc3(str):
#     result = True
#     for i in range(len(str)//2):
#         if str[i] != str[-(i+1)]:
#             result = False
#             break
#     print(result)
# myFunc3("1234321")
# myFunc3("456654")


# def add2(num1, num2):
#     return num1+num2
# print(add2(1,2))


# def single_int():
#     return 3
# def single_float():
#     return 5.5
# def list():
#     return [1, 2, 3]
# def set():
#     return {1, 2, 3}
# def tuple():
#     return 1, 2, 3
# def dictionary():
#     return {"a":1, "b":2, "c":3}
# print(single_int(), type(single_int()))
# print(single_float(), type(single_float()))
# print(list(), type(list()))
# print(set(), type(set()))
# print(tuple(), type(tuple()))
# print(dictionary(), type(dictionary()))


# arr = [10, 20, 3, 4, 5]
# def myReturn(list):
#     min = list[0]
#     for i in range(1, len(list)):   # 이러지말고 list[1:]
#         if list[i] < min:           # 이런걸 사용해야 파이선답다 ㅜㅜ
#             min = list[i]
#     return min
# print(myReturn(arr), type(myReturn(arr)))


# def tup():        # 외부 라이브러리를 이용 할 때 자주 사용한다
#     return 1, 2, 3
# tp = tup()
# print(tp, type(tp))
# x, y, z = tup()
# print(x, y, z, type(x))
# x = 10
# x, _, z = tup()


# list = [1,2,3,4,5]
# def info(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum, sum/len(list)
# sum, avg = info(list)
# print(sum, avg)


# list = [10, 20, 30]
# def min_max(list):
#     min = list [0]
#     max = list [0]
#     for i in list [1:]:
#         if i < min:
#             min = i
#         if i > max:
#             max = i
#     return min, max
# min, max = min_max(list)
# print("min", min, "max", max)


# sum = 0
# def total(values):
#     sum = 0
#     for i in values:
#         sum += i
#     print(sum)

# total([1, 2, 3, 4, 5])
# print(sum)


# sum = 0
# def total2(values):
#     global sum
#     for i in values:
#         sum += i
#     print(sum)
# total2([1, 2, 3])
# print(sum)


# def factorial(num):
#     if num == 0:
#         return num
#     factorial(num-1)
#     print(num)
# print(factorial(5))


# def seikai(n):
#     if n < 3:
#         return n
#     result = 2
#     for i in range(3, n+1):
#         result *= i
#     return result
# print(seikai(5))


# def rc_factorial(n):
#     if n < 3 :
#         return n
#     return n * rc_factorial(n-1)
# print("정답", rc_factorial(5))


# def abs(value):
#     return [v if v > 0 else -v for v in value]
# print(abs([1, 2, 3, -1, 2, -3]))
# print(abs(i for i in range(-3, 3)))
# print((i for i in range(-3, 3)))
# gen = (i for i in range(-3, 3))
# print(gen)  # 제너레이터는 range랑 비슷하고 ...
# print(next(gen), next(gen), next(gen))
# print(gen)  # ui 랑 섞이면 딜레이를 줘서 할 수 있다.