import numpy as np


def main():
    N, M, K = map(int, input().split())
    x = []

    for i in range(N):
        x.append(list(map(int, input().split())))
    
    satisfied_money = []

    # bit全探索
    # @see https://qiita.com/gogotealove/items/11f9e83218926211083a
    for i in range(2**N):
        tmp = []
        for j in range(N):
            # bit on-off
            if (i>>j) & 1:
                tmp.append(x[j])

        if tmp != []:
            tmp = np.array(tmp)
            tmp = np.sum(tmp, axis=0)
            # 全ての列で条件をクリアしているか？
            if (tmp[1:] >= K).all():
                satisfied_money.append(tmp[0])
        else:
            continue
        
    if satisfied_money == []:
        print(-1)
    else:
        print(np.min(satisfied_money))


if __name__ == "__main__":
    main()