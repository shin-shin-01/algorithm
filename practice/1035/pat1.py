## TLE

def main():
    ## input
    N = int(input())
    num = []
    for i in range(N): 
        num.append(int(input()))
        
    ## init
    scores = [0]
    
    for j in range(2**N):
        calculate(N, num, j, scores)
    
    scores = sorted(scores)
    print(len(scores))
    for i in scores: print(i)
    
def calculate(N, num, count, scores):
    score = 0
    for i in range(N):
        ## ２進数化 * 各問Point
        score += (count // (2**i) % 2) * num[i]
        
    if not score in scores:
        scores.append(score)

if __name__ == "__main__":
    main()