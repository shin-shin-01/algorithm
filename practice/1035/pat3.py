## TLE

import itertools

def main():
    ## input
    N = int(input())
    num = []
    for i in range(N):
        ## 0 or Point
        num.append((int(input()), 0))

    ## デカルト積　（multi args : *num）
    scores = list(itertools.product(*num))
    ## calculate SUM
    scores = map(sum, scores)
    ## del duplications
    scores = list(set(scores))
                
    scores.sort() 
    print(len(scores))
    for i in scores: print(i)
    

if __name__ == "__main__":
    main()
