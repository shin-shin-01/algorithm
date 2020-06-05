import unittest
from io import StringIO
import sys
from timeit import timeit
from random import randint

def main_TLE(A, B, N):
    # A, B, N = map(int, input().split())
    ans = 0

    for x in range(0, N+1):
        a = ( int((A*x)/B) - A*int(x/B) )
        if ans < a:
            ans = a
    
    print(a)


def main():
    A, B, N = map(int, input().split())

    #ans = ( int((A*x)/B) - A*int(x/B) )
    # 第２項はxがBより小さい時に０にできる
    # 第１項はxが大きければ大きいほど良い

    if B <= N:
        x = B - 1
    else:
        x = N
    
    print(int((A*x)/B) - A*int(x/B))


class TestMain(unittest.TestCase):

    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        main()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
        

    def test1_main(self):
        input = """5 7 4"""
        output = """2"""

        self.assertIO(input, output)

    def test2_main(self):
        input = """11 10 9"""
        output = """9"""

        self.assertIO(input, output)


if __name__ == "__main__":
    # loop = 2
    # time = timeit('main_TLE(A=randint(0, 100), B=randint(0, 100), N=randint(0, 100))', globals=globals(), number=loop)
    # print('Time average :', time/loop)
    main()
