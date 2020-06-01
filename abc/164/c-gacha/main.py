from timeit import timeit

def main_TLE():
    N = int(input())

    gifts = []

    for _ in range(N):
        gift = input()

        if gift in gifts:
            pass
        else:
            gifts.append(gift)
        
    print(len(gifts))


def main():
    N = int(input())

    gifts = []

    for _ in range(N):
        gifts.append(input())
  
    print(len(set(gifts)))


if __name__ == "__main__":
    # loop = 2
    # time = timeit('main_TLE()', globals=globals(), number=loop)
    # print("実行時間: ", time/loop)
    main()