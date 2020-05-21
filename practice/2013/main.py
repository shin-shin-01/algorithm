def main():
    a, b, c = map(int, input().split())
    N = int(input())

    tardy_time = 9*60 + 0

    for _ in range(N):
        h, m = map(int, input().split())
        
        if h*60+m + b + c < tardy_time:
            train = h*60 + m
        else:
            break
        
    ans = train - a
    print(f'{(str(ans//60)).rjust(2, "0")}:{(str(ans%60)).rjust(2, "0")}')


if __name__ == "__main__":
    main()

