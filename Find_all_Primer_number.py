"""
Find all Prime numbers

輸入一正整數，找出所有小於或等於的質數。
"""

int_pr = int(input("Please enter a number, \n"
                   "I'll find out all prime number equal to or below it for you:"))
prime_number = 1

for i in range(1, int_pr+1):
    if i == 1:
        prime_number = 0
    elif i == 2:
        prime_number = 1
    else:
        for j in range(2, i):
            if (i % j) == 0:
                prime_number = 0
                break
            else:
                prime_number = 1
                continue

    if prime_number == 1:
        print(i, end="\t")
    else:
        pass
        # print(i, "is not a prime number.")
