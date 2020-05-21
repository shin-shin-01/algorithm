
import unittest
import sys
from io import StringIO

# from pat1 import main
# from pat2 import main
from pat3 import main

class Testmain(unittest.TestCase):

    def assertIO(self, input, output):
        stdin, stdout = sys.stdin, sys.stdout
        sys.stdin, sys.stdout = StringIO(input), StringIO()
        main()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdin, sys.stdout = stdin, stdout
        self.assertEqual(out, output)

    def test1(self):
        input = """4
6
14
25
55"""
        output = """16
0
6
14
20
25
31
39
45
55
61
69
75
80
86
94
100"""
        self.assertIO(input, output)

    def test2(self):
        input = """4
25
25
25
25"""
        output = """5
0
25
50
75
100"""
        self.assertIO(input, output)
    