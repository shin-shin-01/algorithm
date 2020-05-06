def main():
    N, K = map(int, input().split())
    ## Time_reduction
    N = N % K
    
    while(N > abs(N-K)):
        N = abs(N-K)
    
    print(N)

if __name__ == "__main__":
    main()