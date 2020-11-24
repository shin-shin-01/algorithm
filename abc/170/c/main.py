def main():
    X, N = map(int, input().split())
    p_lst = set(map(int, input().split()))

    minus = []
    plus = []

    for p in p_lst:
        if p - X == 0:
            plus.append(0)
            minus.append(0)
        if p - X > 0:
            plus.append(abs(p - X))
        else:
            minus.append(abs(p - X))
        
    for i in range(1000):
        if not i in minus:
            print(X - i)
            break
        elif not i in plus:
            print(X + i)
            break
        else:
            pass

if __name__ == "__main__":
    main()
