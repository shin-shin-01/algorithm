def main():
    N = int(input())

    a = list(map(int, input().split()))
    anslst = [0]*(N-1)

    for i in a:
        anslst[i-1] += 1

    for ans in anslst:
        print(ans)

    print(0)

if __name__ == "__main__":
    main()