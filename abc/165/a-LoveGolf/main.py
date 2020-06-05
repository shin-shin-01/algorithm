def main():
  K = int(input())
  A, B = map(int, input().split())
  
  remain = A % K
  
  if (remain == 0) or (A + (K- remain) <= B):
    print('OK')
  else:
    print('NG')


if __name__ == "__main__":
  main()
