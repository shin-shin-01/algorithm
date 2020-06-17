import unittest
from io import StringIO
import sys

def main():
    N, way = map(int, input().split())
    high = list(map(int, input().split()))
    ans = [1]*N

    for _ in range(way):
        a, b = map(int, input().split())
        if high[a-1] < high[b-1]:
            ans[a-1] = 0
        elif  high[a-1] > high[b-1]:
            ans[b-1] = 0
        else:
            ans[a-1], ans[b-1] = 0, 0
    
    print(sum(ans))


class TestMain(unittest.TestCase):
    def assertIO(self, input, output):
        stdin, stdout = sys.stdin, sys.stdout
        sys.stdin, sys.stdout = StringIO(input), StringIO()
        main()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdin, sys.stdout = stdin, stdout 
        self.assertEqual(out, output)
    
    def test1_main(self):
        input = """4 3
1 2 3 4
1 3
2 3
2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test2_main(self):
        input = """6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6"""
        output = """3"""
        self.assertIO(input, output)



if __name__ == "__main__":
    main()