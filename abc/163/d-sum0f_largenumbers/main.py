""" Memo
itertools.combinations 遅い
sum(range(0, 4)) 遅い

k*((N+1-k)+N)//2 速い
""" 

import unittest
from io import StringIO
import sys


def main():
    N, K = map(int, input().split())
 
    ans = 0
    mod = pow(10,9)+7
    
    for k in range(K, N+2): ## K個以上で総数(N+1)
        ## 全個数の計算　## k個最大 ## k個最小
        ans += k*((N+1-k)+N)//2 - k*(0+k-1)//2 + 1
        
    print(ans % mod)


class TestMain(unittest.TestCase):
    def assertIO(self, input, output):
        stdin, stdout = sys.stdin, sys.stdout
        sys.stdin, sys.stdout = StringIO(input), StringIO()
        main()
        sys.stdout.seek(0)## オブジェクトの位置
        out = sys.stdout.read()[:-1]
        sys.stdin, sys.stdout = stdin, stdout
        self.assertEqual(out, output)

    def test1_main(self):
        input = """3 2"""
        output = """10"""
        self.assertIO(input, output)
    
    def test2_main(self):
        input = """141421 35623"""
        output = """220280457"""
        self.assertIO(input, output)

    def test3_main(self):
        input = """200000 200001"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    main()
