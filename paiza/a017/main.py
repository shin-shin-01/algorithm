## A017:落ちものシミュレーション
import unittest
import sys
from io import StringIO


def main():
    H, W, N = map(int, input().split())

    stage = [['.' for i in range(W)] for j in range(H)]

    for n in range(N):
        h, w, x = map(int, input().split())
        
        for under in range(H):
            if '#' in stage[under][x:x+w]:
                break
            else:
                under += 1
        
        for i in range(under-h,under):
            stage[i][x:x+w] = list('#'*w)

    ## Print Stage
    for lst in stage:
        for i in range(W):
            print(lst[i], end='')
        print()

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
        input = """7 10 4
1 8 1
4 1 5
1 6 2
2 2 0"""
        output = """..........
..######..
.....#....
.....#....
##...#....
##...#....
.########."""

        self.assertIO(input, output)

    def test2_main(self):
        input = """10 10 9
2 2 4
2 2 3
2 2 5
2 2 2
2 2 6
2 2 1
2 2 7
2 2 0
2 2 8"""
        output = """##......##
##......##
.##....##.
.##....##.
..##..##..
..##..##..
...####...
...####...
....##....
....##...."""

        self.assertIO(input, output)

if __name__ == "__main__":
    main()

