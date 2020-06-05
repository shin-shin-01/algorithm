import itertools
## product 順番あり 重複あり（全て）
## premutations 順番あり 重複なし
## combinations 順番なし　重複なし
## combinations_with_replacement 順番なし　重複あり

def main():
    N, M, Q = map(int, input().split())

    lst = []
    for _ in range(Q):
        lst.append( list(map(int, input().split())) )

    A_pattern = itertools.combinations_with_replacement(range(1, M+1), N)
    ans = 0

    for a in A_pattern:
        point = 0
        
        for l in lst:
            if a[l[1]-1] - a[l[0]-1] == l[2]:
                point += l[3]
            
        if ans < point:
            ans = point

    print(ans)


if __name__ == "__main__":
    main()