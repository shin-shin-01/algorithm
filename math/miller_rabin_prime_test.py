"""
ミラーラビンの素数判定法

==== 方法 =====
ここあとでまとめよう

==== 確率 =====
nが合成数なのに素数の可能性があると判定してしまう確率は
最大で 4^(-k)
"""

import random

def is_prime(n):
    if n == 2: return True
    ## 偶数判定: n&1 == 0
    if n == 1 or n & 1 == 0: return False

    ## n - 1 = 2^s * d : dは奇数
    d = (n-1) >> 1  ## /2
    while d & 1 == 0:
        d >>= 1

    for _ in range(100):
        a = random.randint(1, n-1)
        t = d
        y = pow(a, t, n)

        while t != n-1 and y != 1 and y != n-1:
            y = (y * y) % n
            t <<= 1

        if y != n-1 and t & 1 == 0:
            return False

    return True


if __name__ == "__main__":
    print(is_prime(2 ** 89 -1))