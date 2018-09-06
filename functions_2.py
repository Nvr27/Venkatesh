# import math
#
# def faction(n):
#     a=math.factorial(n)
#     return a
# print(faction(10))
# def sumnum(x):
#     count=0
#     for i in range(len(x)):
#         count=count+x[i]
#     return count
# x=[10,20,30,60,80,90]
# print(sumnum(x))

def fun(x):
    if x < 10:
        return 1
    return 1 + fun(x / 10)


print(fun(123))
