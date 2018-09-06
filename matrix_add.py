matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        matrix2[i][j] = matrix2[i][j] + matrix1[i][j]
print(matrix2)

list = [5, 8, 5, 6, 8, 2, 3, 5, 1, 0, 2, 8, 9, 4, 7]
for i in range(0, 14):
    if list[i] > list[i + 1]:
        a = list[i]
        list[i] = list[i + 1]
        list[i + 1] = a
print(list)
list = ["sai", "venkatesh", "reddye", "super", "manoj"]
list1 = []
for i in list:
    list1.append(i)
list1.sort(key=len)
print(list1)
