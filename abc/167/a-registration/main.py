def main():
    S = input()
    T = input()
    
    if S == T[:-1]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()