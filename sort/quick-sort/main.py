import numpy as np
import unittest
import random

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        ## pivot = lst[0]
        left, right = [], []
        
        for i in range(1, len(lst)):
            if lst[i] <= lst[0]:
                left.append(lst[i])
            else:
                right.append(lst[i])

        left = quick_sort(left)
        right = quick_sort(right)

        return left + [lst[0]] + right

class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        """クイックソートのテスト"""
        length = random.randint(0, 10)
        lst = np.random.randint(0, 30, length)
        lst = quick_sort(lst)
        self.assertEqual(sorted(lst), list(quick_sort(lst)))
        

if __name__ == "__main__":
    print('Quick Sort')
    length = random.randint(0, 10)
    lst = np.random.randint(0, 30, length)
    lst = quick_sort(lst)
    print(lst)