# def merge(list, low, mid, high):
#     l=low
#     r=mid+1
#     temp=[]
#     while l <= mid and r <= high:
#         if list[l] < list[r]:
#             temp.append(list[l])
#             l += 1
#         else:
#             temp.append(list[r])
#             r += 1
#     if l > mid:
#         temp.extend(list[r:high+1])
#     elif r > high:
#         temp.extend(list[l:mid+1])
#     list[low:high+1] = temp
#     print(list)
# def merge_sort(list, low, high):
#     if low >= high:
#         return
#     mid = (low+high)//2
#     merge_sort(list, low, mid)
#     merge_sort(list, mid+1, high)
#     merge(list, low, mid, high)

# list = [8, 7, 6, 5, 4, 3, 2, 1]
# merge_sort(list, 0, 7)       