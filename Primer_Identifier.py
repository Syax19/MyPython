"""
2. 函數的練習-is_prime

寫一函數is_prime(n)用來判斷n是否為質數。
"""


def is_prime(n):
    prime_num = 1
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if (n % i) == 0:
                prime_num = 0
                break
            else:
                prime_num = 1
                continue
        if prime_num == 0:
            return False
        else:
            return True


if __name__ == "__main__":
    ans_1 = is_prime(2047)
    print(ans_1)
    ans_2 = is_prime(19)
    print(ans_2)
