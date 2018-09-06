# list1 = [20, 50, 80, 10, 20, 50, 60]
#
# for i in range(0,6):
#     if list1[i] > list1[i + 1]:
#         a = list1[i]
#         list1[i] = list1[i + 1]
#         list1[i + 1] = a
# print(list1)
# list2=[10,20,30,50,60,40,60,80,50,1]
# list1=[]
# for i in range(0,10):
#     # a=set(list[i])
#     list1.append(list2[i])
#
# a=list(set(list1))
# print(a)
# list1 = ["venkatesh", "manoj", "sai"]
# list = []
# for i in list1:
#     list.append(i)
# print(max(list))
list=[10,20,30]
for i in range(0,3):
    inches=list[i]*0.32
    f=list[i]*1.8+32
    print(round(inches,2))

    print(f)

    try:
        if (list[i]%i==0):
            print(i)
    except:
        print("this is error")

