import sys
import unittest
from io import StringIO


def main():
    N, X, Y = map(int, input().split())

    X -= 1
    Y -= 1

    output = [0]*N

    for i in range(N-1):
        for j in range(i+1, N):
            output[min((j-i), abs(i-X)+1+abs(j-Y))] += 1
        
    for i in range(1, N):
        print(output[i])


class Testmain(unittest.TestCase):

    def assertIO(self, input, output):
        stdin, stdout = sys.stdin, sys.stdout
        sys.stdin, sys.stdout = StringIO(input), StringIO()
        main()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdin, sys.stdout = stdin, stdout
        self.assertEqual(out, output)

    def test1_main(self):
        input = """5 2 4"""
        output = """5
4
1
0"""
        self.assertIO(input, output)

    def test2_main(self):
        input = """3 1 3"""
        output = """3
0"""
        self.assertIO(input, output)

    def test3_main(self):
        input = """10 4 8"""
        output = """10
12
10
8
4
1
0
0
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    main()