value=["venkatesh","sai","pavan","manoj"]
value1=value
value2=value1
value1[0]="chinna"
value2[1]="bob"
sum=0
for i in range(0,len(value1)):
    if i=="chinna":
        sum+=1
    if i=="bob":
        sum+=1
print(sum)