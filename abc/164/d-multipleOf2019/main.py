def main_TLE():
    S = input()

    ans = 0

    ## 4桁
    for i in range(0, len(S)-3):
        for j in range(i+3, len(S)):
            if int(S[i:j+1]) % 2019 == 0:
                ans += 1

    print(ans)


def main():
    S = input()[::-1]
 
    ## 余りを0~2018で総数保持
    counts = [0]*2019
    ## 0桁の余りは0
    counts[0] = 1

    num, d = 0, 1
 
    for c in S:
        ## 右から~桁の数字
        num += int(c) * d
        num %= 2019
        ## 次の桁
        d *= 10
        d %= 2019
  
        counts[num] += 1
  
    ans = 0

    for cnt in counts:
        ## nC2の計算
        ans += cnt * (cnt-1) //2
  
    print(ans)


if __name__ == "__main__":
    main()