"""
factorial (n)可計算1*2*3*…*n的值。

"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


fac_ans = factorial(6)
print(fac_ans)
