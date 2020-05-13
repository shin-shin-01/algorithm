from math import gcd
import timeit

def main(K):
    # K = int(input())
    Sum = 0

    for i in range(1, K+1):
        for j in range(1, K+1):
            s = gcd(i, j) ## point!
            for l in range(1, K+1):
                Sum += gcd(s, l)

    return Sum


if __name__ == "__main__":
    ## 時間計測用
    K = int(input("入力 : "))
    print("出力 : ", main(K))

    t = timeit.timeit(lambda: main(K), number=5)
    print("実行時間 {}".format(t/5))