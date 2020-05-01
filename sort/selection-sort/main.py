import numpy as np
import random
import unittest

def selection_sort(lst):
    for i in range(0, len(lst)):
        minimum = i

        for j in range(i, len(lst)):
            if lst[minimum] > lst[j]:
                minimum = j
            else:
                pass
        lst[i], lst[minimum] = lst[minimum], lst[i]

    return lst

class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        """セレクションソートのテスト"""
        length = random.randint(0, 10)
        lst = np.random.randint(0, 30, length)

        self.assertEqual(sorted(lst), list(selection_sort(lst)))

if __name__ == "__main__":
    print('SelectionSort')
    length = random.randint(0, 10)
    lst = np.random.randint(0, 30, length)
    lst = selection_sort(lst)
    print(lst)