def main():
    X = int(input())

    money = 100
    ans = 0

    while money < X:
        money = int(money*1.01)
        ans += 1
        
    print(ans)

if __name__ == "__main__":
    main()