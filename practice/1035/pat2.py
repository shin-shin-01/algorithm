## TLE

import itertools

def main():
    ## input
    N = int(input())
    num = []
    for i in range(N):
        num.append(int(input()))
    
    ## init
    scores = [0]

    ## Combination 個数でループ    
    for n in range(N):
        ## 個数(n+1) Combination: nCr
        for tup in itertools.combinations(num, n+1):
            if not sum(tup) in scores:
                scores.append(sum(tup))
                
    scores = sorted(scores)
    print(len(scores))
    for i in scores: print(i)


if __name__ == "__main__":
    main()