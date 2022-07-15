"""
Finding the perfect number

一個數字若等於其所有因數的總和，則此數為perfect number。
找出100以內所有的完美數。

說明：6的因數為1, 2, 3，6=1+2+3，故6為完美數。
"""
pf = 0
for number in range(1, 100+1):
    for i in range(1, number):
        if ((number % i) == 0) and (i == 1):
            pf = 1
        elif (number % i) == 0:
            pf = pf + i

    if pf == number:
        print(number, "為完美數")
    else:
        pass
        # print(number, "不是完美數")

