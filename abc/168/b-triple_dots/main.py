def main():
    K = int(input())
    S = input()

    if len(S) <= K:
        print(S)
    else:
        print(f'{S[:K]}...')


if __name__ == "__main__":
    main()