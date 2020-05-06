def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    minimum = sum(A) / (4*M)

    for i in A:
        if i >= minimum:
            M -= 1
        
    if M > 0:
        print('No')
    else:
        print('Yes')

if __name__ == "__main__":
    main()