n = 25
# a = 0
# b = 1
# while a < n:
#     print(a)
#     a, b = b, a + b

for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            print("this is not prime number", i)
            break
    else:
        print("this is prime number", i)
