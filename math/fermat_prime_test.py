"""
フェルマーテスト

==== 方法 =====
2からn-1までの数から a をランダムに選ぶ
aとnの間で
「最大公約数が１かどうか」
「フェルマーの小定理が成り立つかどうか」

- どちらの条件も満たせば「n」は素数である

※　フェルマーの小定理は 素数pと互いに素な整数aの間で必ず成り立つ

==== 確率 =====
合成数でもフェルマーの小定理が成立することもあり
そのような合成数を「擬素数」という
どのようなaに対しても成立する擬素数を「絶対擬素数」という

１回の試行に合格するとそれが素数である確率は1/2以上
"""


import random

def original_gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def is_prime(n):
    if n == 1: return False
    if n == 2: return True

    ## 100回繰り返す
    for _ in range(100):
        a = random.randint(2, n-1)

        if original_gcd(n, a) != 1:
            return False

        if pow(a, n-1, n) != 1:
            return False

    return True

if __name__ == "__main__":
    print(is_prime(2**89 -1))