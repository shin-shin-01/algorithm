import sys
from io import StringIO
import unittest

def main():
    money = int(input())
    hapiness = (money//500)*1000 + ((money%500)//5)*5
    print(hapiness)

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
        input = """1024"""
        output = """2020"""
        self.assertIO(input, output)

    def test2_main(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)
    
    def test3_main(self):
        input = """1000000000"""
        output = """2000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    main()