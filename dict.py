# dic={1:"a",2:"b",3:"c",4:"d"}
# d={}
# d.update(dic)
# print(d)
# d={4:"a",5:"f"}
# dic.update(d)
# print(dic)
# d=int(input("enter the keys:"))
# if d in dic.keys():
#     print("keys are thers:")
#     print(dic[d])
# else:
#     print("enter the number")
# n=10
# dic={x:x*x for x in range(n+1)}
# print(dic)
# n={"a":10,"b":15,"c":250}
# sum=0
# count=1
# sum1=100
# for i in n:
#     sum+=n[i]
#     count*=n[i]
#     sum1-=n[i]
# print(sum)
# print(count)
# print(sum1)
# dict={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}
# dict1=input("enter the number:")
# if dict1 in dict:
#     del dict[dict1]
# else:
#     print("this key is not present:")
#     exit(0)
# print(dict)

class a(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
obj=a(1,2)
print(obj.__dict__)






























