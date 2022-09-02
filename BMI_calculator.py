ans = "1"

while ans == "1":
    height = float(input("請輸入身高(cm): "))
    weight = float(input("請輸入體重(kg): "))

    BMI = weight / (height/100)**2

    print("您的身高為:", height, "(cm)", "\t體重為:", weight, "(kg)")
    print("BMI值為:", BMI)

    if 0 < BMI < 18.5:
        print("*****體重過瘦*****")
    elif 18.5 <= BMI < 24:
        print("*****體重標準*****")
    elif 24 <= BMI < 27:
        print("*****體重過重*****")
    elif 27 <= BMI < 30:
        print("*****輕度肥胖*****")
    elif 30 <= BMI < 35:
        print("*****中度肥胖*****")
    elif BMI >= 35:
        print("*****重度肥胖*****")
    else:
        print("請檢查輸入的身高體重之數值")

    ans = input("請輸入執行代碼(1.繼續 2.停止):")
    if ans == "1":
        ans = "1"
    elif ans == "2":
        break
    else:
        print("輸入錯誤請重新輸入")
        ans = input("請輸入執行代碼(1.繼續 2.停止):")
        while (ans != "1") and (ans != "2"):
            ans = input("請輸入執行代碼(1.繼續 2.停止):")
