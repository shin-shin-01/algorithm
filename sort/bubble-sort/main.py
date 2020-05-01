import unittest
import random
import numpy as np

def bubble_sort(lst):
    ## 回数
    for i in range(0, len(lst)):
        ## 比較セル
        for j in range(0, len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            else:
                pass
    return lst 

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        """バブルソートのテスト"""
        length = random.randint(0, 10)
        lst = np.random.randint(0, 30, length)
        
        self.assertEqual(sorted(lst), list(bubble_sort(lst)))


if __name__ == "__main__":
    print('BubbleSort')
    length = random.randint(0, 10)
    lst = np.random.randint(0, 30, length)
    lst = bubble_sort(lst)
    print(lst)