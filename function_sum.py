# def fun(n):
#     sum = 0
#     while n > 0:
#         a = n % 10
#         sum=sum+a
#         n=n//10
#     return sum
# print(fun(123))
# def fun(x):
#     if x < 10:
#         return 1
#     return 1 + fun(x / 10)
# print(fun(123))
# def fun(n):
#     for i in range(2,n):
#         for j in range(2,i):
#             if i%j==0:
#                 print("this not a prime number",i)
#                 break
#         else:
#             print("this number is primenumber",i)
# fun(100)
# def fun(x):
#     if len(x)<=1:
#
#         return True
#
#     if x[0]!=x[-1]:
#
#         return False
#     return fun(x[1:len(x)-1])
# print(fun("mom"))

def fun(x):
    str=""
    for i in x:
        str=i+str
    return str
print(fun("venkatesh"))














