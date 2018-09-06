a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
c=0
# for i in a,b:
#     (c.append(i))
#     print(c)

print("-------------------------------")

# for j in a,b:
#     (c.extend(j))
#     print(c)

# for i in b:
#     c.insert(i,b)
#     print(c)

for i in range(0,len(b)):
    for j in range(0,len(a)):
        print(b[i],end="=")
        print(a[j])
