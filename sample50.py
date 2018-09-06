# for i in range(0,10):
#     if i%2!=0:
#         print(i)
# n=int(input("enter the number:"))
# total=0
# while n>0:
#     a=n%10
#     total=total+a
#     n=n//10
# print(total)

def intersection(a, b):
    return list(set(a) & set(b))

# def main():
#
#     a=[1,5,8,9,8,7,2,3,8,9]
#     b=[8,2,1,3,0,7,8,7,8]
#     list1 = []
#     list2=[]
#     for i in range(0,10):
#         # list1[i]=list1[i]+a[i]
#         c=str(i)
#         list1.append(c)
#     for j in range(0,9):
#         # list2[j]=list2[j]+b[j]
#         d=str(j)
#         list2.append(d)
#
#
#     print(intersection(list1, list2))
#
#
# main()
# a=[1,5,8,9,6,3,2]
# b=[2,5,8,5,0]
#
# c = [2,5,8]



a = [ 1,2,3,4,5,6]
b = [7,3,4,2,5,8]
# c = []
#
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#
# print(c)

print(intersection(a,b))





