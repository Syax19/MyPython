"""
mersenne_prime

is_mersenne_prime(n)用來判斷n是否為Mersenne質數。
get_mersenne_prime(n)用來獲取前n個Mersenne質數。

說明：若質數滿足2^P-1=n (p為正整數)，則n為Mersenne Prime。
    當p=3時，2^3-1=7，故7為Mersenne Prime。
"""

from Homework_3_2 import is_prime


def is_mersenne_prime(n):
    num = 2
    mp_list = []
    while True:
        mp_num = (2 ** num) - 1
        if is_prime(mp_num) is True:
            mp_list.append(mp_num)

        num += 1

        if n in mp_list:
            return True
        elif max(mp_list) > n:
            return False


def get_mersenne_prime(n):
    num = 2
    mp_list = []
    while True:
        mp_num = (2 ** num) - 1
        if is_prime(mp_num) is True:
            mp_list.append(mp_num)

        num += 1

        if len(mp_list) == n:
            return mp_list


if __name__ == "__main__":
    ans_1 = get_mersenne_prime(5)
    print(ans_1)

    ans_2 = is_mersenne_prime(11)
    print(ans_2)
