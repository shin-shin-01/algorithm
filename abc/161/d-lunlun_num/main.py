### コツは実際に書いてみること
### 二桁の数までで法則がわかるはず

import unittest
import sys
from io import StringIO

def main():
    K = int(input())

    # init
    lst = [[i for i in range(1,10)]]
    total=9

    ## 8: 7, 8, 9
    ## 9: 8, 9
    ## 0: 0, 1

    while total < K:
        lst.append([])
        for i in lst[-2]:
            strnum = str(i)
            last = int(strnum[-1])
            
            lst[-1].append(strnum + str(last))
            if last <= 8:
                lst[-1].append(strnum + str(last+1))
            if last >= 1:
                lst[-1].append(strnum + str(last-1))
                
        total += len(lst[-1])

    lst[-1].sort()
    print(lst[-1][K-total-1])


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
        input = """13"""
        output = """21"""
        self.assertIO(input, output)

    def test2_main(self):
        input = """100000"""
        output = """3234566667"""
        self.assertIO(input, output)

    def test3_main(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    main()