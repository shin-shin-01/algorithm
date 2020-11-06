def main():
    import sys

    n = int(input())
    nums = list(map(int, input().split()))
    nums = sorted(nums, reverse=True)

    if 0 in nums:
        print(0)
        sys.exit()

    answer = 1
    for n in nums:
        answer *= n
        if answer > 10**18:
            print(-1)
            sys.exit()
    
    print(answer)


if __name__ == "__main__":
    main()
