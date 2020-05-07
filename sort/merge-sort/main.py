import numpy as np
import unittest
import random

def merge(left, right):
    lst = []

    if type(left) != list:
        left = [left]
    if type(right) != list:
        right = [right]

    i = left[0]
    j = right[0]

    while True:
        try:
            if i <= j:
                lst.append(i)
                left.pop(0)
                i = left[0]
            else:
                lst.append(j)
                right.pop(0)
                j = right[0]

        except IndexError:
            return lst + left + right    


def merge_sort(lst):
    lst = list(lst)

    if not lst: ## EmptyList
        return []

    while len(lst) > 1:

        for i in range(len(lst)//2):
            lst[i*2] = merge(lst[i*2], lst[i*2+1])

        lst = lst[::2]

    return lst[-1]
    

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        """マージソートのテスト"""
        length = random.randint(0, 10)
        lst = np.random.randint(0, 30, length)
        self.assertEqual(sorted(lst), list(merge_sort(lst)))


if __name__ == "__main__":
    print('Merge Sort')
    length = random.randint(0, 10)
    lst = np.random.randint(0, 30, length)
    lst = merge_sort(lst)
    print(lst)