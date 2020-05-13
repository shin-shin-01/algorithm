def main():
    N = int(input())

    Sum = 0
    for i in range(1, N+1):
        if (i%3 != 0) and (i%5 != 0):
            Sum += i
            
    print(Sum)


if __name__ == "__main__":
    main()