# str1 = "venkatesh"
# str2 = "reddymmmmm"
# count1 = 0
# count2 = 0
# for i in str1:
#     count1 = count1 + 1
# for j in str2:
#     count2 = count2 + 1
# if count1 > count2:
#     print(str1)
# else:
#     print("In else block")
#     print(str2)

# str1="VenkaTesh"
# count=0
# count1=0
# for i in str1:
#     if i.islower():
#         count=count+1
#     if i.isupper():
#         count1=count1+1
# print(count)
# print(count1)


# str1 = "dad2"
# str2=str1[::-1]
# if str1 == str2:
#     print("TRUE")
# else:
#     print("false")

# str1 = "venkatesh"
# str2 = ""
# for i in str1:
#     str2 += i
# a=sorted(str1)
# print("-".join(a))

str1="venkatesh1234"
count1=0
count2=0
for i in str1:
    if i.isdigit():
        count1+=1
    else:
        count2+=1
print(count1)
print(count2)