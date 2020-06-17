"""オーダーに関して
O(N) の場合 N≦10^(7)
"""

def main():
    x = int(input())

    """
    求めるxが10^(9)以下
    y = a^5-b^5 に関して，a を大きくしつつ y を小さくするのは
    b = a-1 の時であり，yが10^(9) を恒久的に超えるのは
    a が 200以上の時のため，以下の範囲で限定してよい！

    -200<=b<=200 , 0<=a<=200
    -> 10^2 * 10^2 : O(10^4)
    """

    for a in range(0, 200):
        for b in range(-200, 200):
            if (a**5 - b**5 == x):
                print(a, b)
                exit()

    print('該当なし')


def calc(x):
    ## 200くらいまで
    ans = x**5 - (x-1)**5
    print("5乗計算:", ans)
    print('10^9　以下' if ans <= 10**9 else '10^9 を超えてます')


if __name__ == "__main__":
    # i = int(input("calc:"))
    # calc(i)
    main()