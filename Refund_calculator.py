"""
Refund
### 若有其他幣值可以自行新增或修改 ###

輸入在某商店購物應付金額與實付金額。
實付金額小於應付金額，則印出”金額不足”。
實付金額等於應付金額，則印出”不必找錢”。
實付金額大於應付金額，則輸出找回金額最少的鈔票數和錢幣數。
假設幣值只有1000, 500, 100元紙鈔和50, 10, 5, 1元硬幣。

說明：若買了132元的商品，付1000元，應找回一張500元，三張100元，一個50元硬幣，一個10元硬幣，一個5元硬幣和三個1元硬幣。
"""
cost = int(input("應付金額:"))
pay = int(input("實付金額:"))

if cost > 0 and pay > 0:
    if pay < cost:
        print("金額不足")
    elif pay == cost:
        print("不必找錢")
    elif pay > cost:
        refund = (pay - cost)
        print("應找回金額:", refund)

        bill_1000 = (refund//1000)
        refund_fh = (refund - ((refund//1000) * 1000))

        bill_500 = (refund_fh//500)
        refund_h = (refund_fh - ((refund_fh//500) * 500))

        bill_100 = (refund_h // 100)
        refund_fc = (refund_h - ((refund_h//100) * 100))

        coin_50 = (refund_fc // 50)
        refund_t = (refund_fc - ((refund_fc // 50) * 50))

        coin_10 = (refund_t // 10)
        refund_f = (refund_t - ((refund_t // 10) * 10))

        coin_5 = (refund_f // 5)

        coin_1 = (refund_f - ((refund_f // 5) * 5))

        print(f"找您: {bill_1000}張千元鈔, {bill_500}張五百元鈔, {bill_100}張百元鈔, {coin_50}個五十元, {coin_10}個十元, {coin_5}個五元, {coin_1}個一元")
    else:
        print("請檢查輸入資料")
else:
    print("請檢查輸入金額")
