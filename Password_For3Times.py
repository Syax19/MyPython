"""
Password

出現”請輸入密碼”的提示，使用者有最多三次輸入的機會。
若輸入正確，則印出”密碼輸入正確，歡迎使用本系統！”。
若輸入不正確，再次出現”請輸入密碼”的提示。
若三次輸入不正確，則印出”密碼輸入超過三次！”，並結束程式的執行。

以下提供使用for loop以及while loop兩種方式寫的code。
"""


##### for loop #####
password = input("請建立密碼:")

for i in range(3+1):
    if i == 3:
        print("密碼輸入超過三次！")
        break
    else:
        pass_input = input("請輸入密碼(最多三次輸入機會):")
        if password == pass_input:
            print("密碼輸入正確，歡迎使用本系統！")
            break
        elif password != pass_input:
            continue


##### while loop #####
password = input("請建立密碼:")

j = 0

while j == 0 or j == 1:
    pass_input = input("請輸入密碼(最多三次輸入機會):")
    if password == pass_input:
        print("密碼輸入正確，歡迎使用本系統！")
        break
    elif password != pass_input:
        j += 1
        if j == 2:
            pass_input = input("請輸入密碼(最多三次輸入機會):")
            if password != pass_input:
                print("密碼輸入超過三次！")
                break
            else:
                print("密碼輸入正確，歡迎使用本系統！")
                
