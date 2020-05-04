import sys
from io import StringIO
import unittest


def main():
    s = input()

    if (s[2] == s[3]) and (s[4] == s[5]):
        print('Yes')
    else:
        print('No')


class Testmain(unittest.TestCase):

    def assertIO(self, input, output):
        ##　退避
        stdout, stdin = sys.stdout, sys.stdin
        ##  StringIO で上書き
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        main()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test1_main(self):
        input = """sippuu"""
        output = """Yes"""

        self.assertIO(input, output)

    def test2_main(self):
        input = """iphone"""
        output = """No"""

        self.assertIO(input, output)

if __name__ == "__main__":
    main()