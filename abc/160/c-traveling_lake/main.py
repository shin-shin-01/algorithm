import sys
from io import StringIO
import unittest


def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0]+K)

    maxD = 0
    for n in range(N):
        maxD = max(maxD, A[n+1] - A[n])

    print(K - maxD)

class Testmain(unittest.TestCase):

    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        main()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test1_main(self):
        input = """20 3
5 10 15"""
        output = """10"""
        self.assertIO(input, output)

    def test2_main(self):
        input = """20 3
0 5 15"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    main()

