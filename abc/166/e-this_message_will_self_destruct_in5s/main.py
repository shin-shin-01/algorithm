import itertools
from collections import defaultdict


def main_TLE():
    """
    O(N^2)
    2<= N <=2*10^5
    """
    N = int(input())
    high = list(map(int, input().split()))

    cnt = 0
    for tup in itertools.combinations(range(N), 2):
        if abs(tup[0]-tup[1]) == (high[tup[0]]+high[tup[1]]):
            cnt += 1

    print(cnt)


def main_TLE_2():
    """
    i - j = A[i] + A[j]
    -> i - A[i] = j + A[j]
    i > j
    """
    N = int(input())
    high = list(map(int, input().split()))

    cnt = 0
    calc = []
    for i in range(1, N+1):
        tmp = i - high[i-1]
        calc.append(i + high[i-1])
        if tmp in calc[:-1]:
            cnt += calc[:-1].count(tmp)

    print(cnt)

def main():
    """
    i - j = A[i] + A[j]
    > i - A[i] = j + A[j]
    i > j
    """
    from collections import defaultdict

    N = int(input())
    high = list(map(int, input().split()))

    ans = 0
    calc = defaultdict(int)
    for i in range(1, N+1):
        ans += calc[i - high[i-1]]
        calc[i + high[i-1]] += 1

    print(ans)


if __name__ == "__main__":
    main()