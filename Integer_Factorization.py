"""
Factorization - Find all factors

輸入一正整數，求其所有的因數。
說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36,
"""

int_a = int(input("請輸入一正整數:"))
for i in range(1, int_a+1):
    if (int_a % i) == 0:
        print(i, end=", ")
