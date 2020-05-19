## オーダーがO(N^2)になるようにプログラム作成

import unittest
import sys
from io import StringIO

def main():
    N = int(input())
    S = input()

    ## 組み合わせの総数
    ans = S.count('R') * S.count('B') * S.count('G')

    ## 除外
    ## j - i = k - j 
    ## k = 2*j -i

    for i in range(0, N-2):
        for j in range(i+1, N-1):
            
            if 2*j-i >= N:
                break
            elif S[i] != S[j] and S[j] != S[2*j-i] and S[2*j-i] != S[i]:
                ans -= 1
    
    print(ans)



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
        input = """4
RRBG"""
        output = """1"""

        self.assertIO(input, output)

    def test2_main(self):
        input = """39 
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB"""
        output = """1800"""

        self.assertIO(input, output)


if __name__ == "__main__":
    main()