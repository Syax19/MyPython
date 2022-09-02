"""
Salary calculator
### 使用時可自行更改薪資倍率及工作時數區間 ###

輸入工作時數，並計算其薪資。
60小時以內，時薪160元。
61~80小時，以時薪1.25倍計算。
81小時以上，以時薪1.5倍計算。

說明：薪資以累計方式計算。若工時為90小時，
則薪資為60*160 + 20*160*1.25 + 10*160*1.5元。
"""
base_sal_60 = 60 * 160
base_sal_80 = base_sal_60 + (20 * 160 * 1.25)

wk_time = int(input("請輸入您的工作時數:"))
if 0 <= wk_time <= 60:
    sal = wk_time * 160
    print("您的薪資:", sal)
elif 61 <= wk_time <= 80:
    sal = base_sal_60 + ((wk_time - 60) * 160 * 1.25)
    print("您的薪資:", sal)
elif 81 <= wk_time:
    sal = base_sal_80 + ((wk_time - 80) * 160 * 1.5)
    print("您的薪資:", sal)
else:
    print("請檢查輸入時數是否正確")
