def some_func(a, b):
    c = a+b
    for i in [c]:
        print(sorted(i))
        print(set(i))


a = [10, 20, 30]
b = [20, 30, 40]

new_array = some_func(a, b)
