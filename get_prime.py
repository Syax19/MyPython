"""
get_prime (n)可用來找出第n個質數。
"""


def get_prime(n):
    prime_list = [2]
    prime_num = 1
    num = 3
    while True:
        for i in range(2, num):
            if (num % i) == 0:
                prime_num = 0
                break
            else:
                prime_num = 1
                continue
        if prime_num != 0:
            prime_list.append(num)

        num += 1

        if len(prime_list) == n:
            return "第" + str(n) + "個質數為: " + str(prime_list[n-1])


if __name__ == "__main__":
    prime = get_prime(6)
    print(prime)
