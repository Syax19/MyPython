"""
Electricity Bill
### 使用時可自行修改 "用電類別 ", "計價區間 ", "區間價格" ###

輸入何種用電和度數，計算出需繳之電費。
電力公司使用累計方式來計算電費，分工業用電及家庭用電。

                        家庭用電          工業用電

   120度(含)以下         1.63元             0.5元

   121~330(含)度        2.38元             0.5元

   330度以上            3.52元              0.5元
"""
# 設定121~330(含)度的基本費率
base_fam_elec_120 = 120 * 1.63
# 設定330度以上的基本費率
base_fam_elec_330 = base_fam_elec_120 + (210 * 2.38)

elec_class = input("請輸入您的用電類別(工業用電或家庭用電):")
elec_degree = int(input("請輸入您的用電度數:"))

if elec_class == "家庭用電":
    if 0 <= elec_degree <= 120:
        bill = elec_degree * 1.63
        print("您的用電類別為:{0:^8}\t電費: {1:^8.2f}".format(elec_class, bill))
    elif 121 <= elec_degree <= 330:
        bill = base_fam_elec_120 + ((elec_degree - 120) * 2.38)
        print("您的用電類別為:{0:^8}\t電費: {1:^8.2f}".format(elec_class, bill))
    elif 331 <= elec_degree:
        bill = base_fam_elec_330 + ((elec_degree - 330) * 3.52)
        print("您的用電類別為:{0:^8}\t電費: {1:^8.2f}".format(elec_class, bill))
    else:
        print("請檢查輸入之用電度數是否正確")
elif elec_class == "工業用電":
    if 0 <= elec_degree:
        bill = elec_degree * 0.5
        print("您的用電類別為:{0:^8}\t電費: {1:^8.2f}".format(elec_class, bill))
    else:
        print("請檢查輸入之用電度數是否正確")
else:
    print("請輸入正確的用電類別")
