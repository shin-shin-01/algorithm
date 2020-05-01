import unittest
import numpy as np
import random

def insertion_sort(lst):
    
    for i in range(0, len(lst)):
        left = i - 1
        while left >= 0 and lst[left] > lst[left+1]:
            lst[left], lst[left+1] = lst[left+1], lst[left]
            left -= 1

    return lst

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        """挿入ソートのテスト"""
        length = random.randint(0, 10)
        lst = np.random.randint(0, 30, length)

        self.assertEqual(sorted(lst), list(insertion_sort(lst)))


if __name__ == "__main__":
    print('Insertion Sort\n')
    length = random.randint(0, 10)
    lst = np.random.randint(0, 30, length)
    lst = insertion_sort(lst)
    print(lst)