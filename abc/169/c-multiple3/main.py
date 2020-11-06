def main():
    n = input().split()
    a = int(n[0])
    s = str(n[1]).split('.')
    b = int(s[0]+s[1])

    answer = int(a*b // 100)
    print(answer)

if __name__ == "__main__":
    main()
