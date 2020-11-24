def main():
    X, Y = map(int, input().split())

    # 1) X = turtle + crane
    # 2) Y = turtle * 4 + crane * 2
    # Y = X * 4 - crane * 2

    crane  = (X*4 - Y) / 2
    turtle = X - crane

    if crane % 1 == 0 and turtle >= 0 and crane >= 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
