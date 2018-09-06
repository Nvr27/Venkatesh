# str1="venkayesh"
# count=0
# for i in str1:
#     count=count+1
# new=str1[0:2]+str1[-2:]
# print(new)
str1=["venkatesh","sai","reddy","manoj","venkatesh"]
str2="venkatesh"
count=0
for i in range(len(str1)):
    if str2==str1[i]:
        count+=1
print(count)
