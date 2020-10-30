def calc_point(A, B, K):

  K -= A
  if K > 0:
    point = A
  else:
    # 元に戻してあげる
    return K + A

  K -= B

  if K > 0:
    return point - K
  else:
    return point


def main():
    A, B, C, K = map(int, input().split())

    point = calc_point(A, B, K)
    print(point)


if __name__ == "__main__":
    main()