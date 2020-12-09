
import unittest
import sys
from io import StringIO

from main import main

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
        input = """2
2
#.
##"""
        output = """#...............
##..............
#.#.............
####............
#...#...........
##..##..........
#.#.#.#.........
########........
#.......#.......
##......##......
#.#.....#.#.....
####....####....
#...#...#...#...
##..##..##..##..
#.#.#.#.#.#.#.#.
################"""

        self.assertIO(input, output)

    def test2(self):
        input = """1
3
#.#
.#.
#.#"""
        output = """#.#...#.#
.#.....#.
#.#...#.#
...#.#...
....#....
...#.#...
#.#...#.#
.#.....#.
#.#...#.#"""

        self.assertIO(input, output)
    