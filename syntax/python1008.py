# def my_range(*a, *b, *c):
#     if c:

#     elif b:

#     elif a:
# # ㅇㅏ니당 ㅠㅠ
# def my_range(*num):
#     # 여기 로직은 알아서 하고
#     while start < end:
#         yield start # 시작점을 설정하자  두개면 시작점, 끝점을 설정 end ! 
#         start += step # step 은 3개 들어왔을 경우
# # ---------------------------------------------------------------------------------

# def add(first, second):
#     return first+second
# def sub(first, second):
#     return first-second
# def executor(func, op, param1, param2):
#     return func[op](param1, param2)
# func = {'+':add, '-':sub}
# print(executor(func, '+', 1, 2))
# print(executor(func, '-', 1, 2))
# print(add)

# # ---------------------------------------------------------------------------------

# def func():
#     value=2
#     def nested_func():
#         nonlocal value
#         value=3
#         print('nested', value)
#     nested_func()
#     print('outer', value)

# # ---------------------------------------------------------------------------------

# selection = int(input())
# if selection == 1:
#     def func():
#         print('hello')
# else:
#     def func():
#         print('bye')
# func()

# # ---------------------------------------------------------------------------------

# def add(num1, num2):
#     return num1+num2
# def sub(num1, num2):
#     return num1-num2
# def selectFunc(select):
#     list = [add, sub]
#     return list[select]
# myIn = int(input())
# print(selectFunc(myIn)(1,2))

# 정영화?? 코드 짜는 방법 ..
# def user: ..
# def name: ..
# menus = [{
#     "연관":"배열",
#     "handler": home # 함수
# },{
#     "생각":"날까",
#     "handler": name # 함수
# }]
# currentMenu=0
# menus[currentMenu][handler]() # 왼쪽부터 함수를  찾아서 () 으로 실행

# # ---------------------------------------------------------------------------------

# list = []
# top = 0
# def push(push):
#     if top < 10:
#         list[top+1] = push
#         top += 1
#     else:
#         print("stack overflow")
# def pop(pop):
#     temp = list[top]
#     list[top] = 0
#     top -= 1
#     return temp
# def top():
#     return print("top data ="+list[top])
# def empty():
#     if top < 9:
#         return print("empty")
#     else:
#         return print("not empty")
# def full():
#     if top == 9
#         return print("full")
#     else:
#         return print("not full")

# # ---------------------------------------------------------------------------------

# list = []
# index = 0
# count = 0
# def put ():
#     if count <10:
#         count += 1
#         if(index == 9):
#             index = -1
#         index += 1
#         list[]

# Binary search
# 이건 한 번 해봐야 알 것 같다.

### _______________________________________________________
# def b_search(value, list, low, high):
#     if low > high:
#         return -1
#     mid = (low+high)//2
#     if list[mid] == value:
#         return mid
#     if list[mid] > value:
#         return b_search(value, list, low, mid-1)
#     else:
#         return b_search(value, list, mid+1, high)

# list=[1, 3, 6, 9, 12, 15, 18, 21]
# print('result index = ', b_search(15, list, 0, 7))
### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^