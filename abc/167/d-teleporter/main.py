def main_TLE():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    now = 1
    visited = []
    visited_flg = False

    for i in range(K):
        bef = now
        now = a[bef-1]
        
        # どこからどこ？線で記憶
        if {"bef":bef,"aft":now} in visited:
            visited_flg = True
            visited_index = visited.index({"bef":bef,"aft":now})
            # ループ前を除外
            loop = list(map(lambda l: l["bef"], visited[visited_index:]))
            bef_loop = visited_index
            break
            
        visited.append({"bef":bef,"aft":now})

    # 一度訪れたことがあるかどうか？
    if visited_flg:
        K = (K-bef_loop) % len(loop)
        # どの街か？ -> index
        now = loop[K]
    
    print(now)


if __name__ == "__main__":
    main_TLE()
