# def check(n):
#
#     for i in range(len(n)):
#         if n[i]%2==0:
#             print("this even number:",n[i])
#         else:
#             print("this number is odd:",n[i])
# n=[10,20,30,50,60,77]
# check(n)
# def count1(string,string2="a"):
#     count=0
#     for i in string:
#         if i in string2:
#             count+=1
#     return count
# string="aaavenkatesh"
# print(count1(string,string2="e"))


def fib(n):

    list1 = [0, 1]
    a = 0
    b = 1
    for i in range(0, n):
        b = a + b
        a = b - a
        list1.append(b)
    return list1


print(fib(10))
