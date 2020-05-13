from itertools import product
from functools import reduce
import math
import timeit

def gcd(tup):
  return reduce(lambda a, b: math.gcd(a, b), tup)

def main(K):
    # K = int(input())
    lst = range(1, K+1)
    Sum = 0

    for tup in product(lst, lst, lst):
        Sum += gcd(tup)
    
    return Sum


if __name__ == "__main__":
    ## 時間計測用
    K = int(input("入力 : "))
    print("出力 : ", main(K))

    t = timeit.timeit(lambda: main(K), number=5)
    print("実行時間 {}".format(t/5))