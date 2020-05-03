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

def shell_sort(lst):
    # init
    h = len(lst) // 2
    while True:
        for i in range(0, h):
            lst[i::h] = insertion_sort(lst[i::h])
            
        if h <= 1:
            break
        else:
            h = h // 2
    
    return lst

class TestShellSort(unittest.TestCase):
    def test_shell_sort(self):
        """シェルソートのテスト"""
        length = random.randint(0, 10)
        lst = np.random.randint(0, 30, length)
        self.assertEqual(sorted(lst), list(shell_sort(lst)))


if __name__ == "__main__":
    print('Shell Sort')
    length = random.randint(0, 10)
    lst = np.random.randint(0, 30, length)
    lst = shell_sort(lst)
    print(lst)