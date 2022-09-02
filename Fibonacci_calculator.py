# 費氏數列
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
# f(n) = f(n-1) + f(n-2)

def fun(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fun(n-1) + fun(n-2)


data = int(input("請問要做到費氏數列第幾項?"))
for i in range(data):
    print(fun(i), end=", ")
