"""
Interest

某人A以10%單利投資100000元，某人B則以5%複利投資100000元。
計算多少年後某人B的投資可以超過某人A，並將此時兩人錢數印出。(27年後)

提示：單利公式：P(1+r*n)    複利公式：P(1+r)^n
P：本金，r：利率，n：多少年

(備註︰(1+r)^n 表示 (1+r) 的 n 次方)
"""

interest_A = 100000 * (1 + 0.1 * 1)
interest_B = 100000 * ((1 + 0.05) ** 1)
n = 1

while interest_A > interest_B:
    n += 1
    interest_A = 100000 * (1 + 0.1 * n)
    interest_B = 100000 * ((1 + 0.05) ** n)


print("{0:^4}年後".format(n))
print("某人A的資產:{0:>10.2f}".format(interest_A))
print("某人B的資產:{0:>10.2f}".format(interest_B))

