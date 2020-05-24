def main():
    N, M = map(int, input().split())

    A = list(map(int, input().split()))

    ans = N - sum(A)

    if ans < 0:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()