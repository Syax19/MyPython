"""
Find All Amstrong Number

Amstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。
找出所有的Amstrong數。

說明：153=1^3+5^3+3^3，故153為Amstrong數。
 (2^3 表示 2 的 3 次方, 3^3 表示 3 的 3 次方)

以下提供使用for loop以及while loop所撰寫之程式碼。
"""

##### for loop #####
for int_am in range(100, 999+1):
    str_am = str(int_am)
    sum_a = (int(str_am[0]) ** 3) + (int(str_am[1]) ** 3) + (int(str_am[2]) ** 3)

    if sum_a == int_am:
        print("{0:^6} is an Armstrong number.".format(str_am))
    else:
        pass
        # print("{0:^6} is not an Armstrong number.".format(str_am))

##### while loop #####
str_am = "100"

while 100 <= int(str_am) <= 999:
    sum_a = ((int(str_am[0])) ** 3) + ((int(str_am[1])) ** 3) + (int(str_am[2]) ** 3)

    if sum_a == int(str_am):
        print("{0:^6} is an Armstrong number.".format(str_am))
    else:
        pass
        # print("{0:^6} is not an Armstrong number.".format(str_am))

    int_am = int(str_am)
    str_am2 = int_am + 1
    str_am = str(str_am2)
