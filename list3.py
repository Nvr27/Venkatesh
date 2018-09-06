# list1=10
# a=0
# for i in range(1,list1):
#     a=a+(1/i)
# print(round(a,2))

print("---------------------------")

n=10
x=2
a=1
for i in range(1,n):
    a=a+(x**i/i)
print(round(a,2))

import math
a=0
for i in range(1,10):
    a=a+(2**i/math.factorial(i))
print(a)
