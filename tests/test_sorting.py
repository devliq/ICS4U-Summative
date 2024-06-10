import unittest
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from radix_sort import radix_sort
from utils import is_sorted

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.data = [5, 2, 9, 1, 5, 6]
        self.sorted_data = sorted(self.data)

    def test_bubble_sort(self):
        bubble_sort(self.data, lambda x: None, lambda: 1)
        self.assertTrue(is_sorted(self.data))

    def test_quick_sort(self):
        quick_sort(self.data, lambda x: None, lambda: 1)
        self.assertTrue(is_sorted(self.data))

    def test_merge_sort(self):
        merge_sort(self.data, lambda x: None, lambda: 1)
        self.assertTrue(is_sorted(self.data))

    def test_selection_sort(self):
        selection_sort(self.data, lambda x: None, lambda: 1)
        self.assertTrue(is_sorted(self.data))

    def test_insertion_sort(self):
        insertion_sort(self.data, lambda x: None, lambda: 1)
        self.assertTrue(is_sorted(self.data))

    def test_heap_sort(self):
        heap_sort(self.data, lambda x: None, lambda: 1)
        self.assertTrue(is_sorted(self.data))

    def test_radix_sort(self):
        radix_sort(self.data, lambda x: None, lambda: 1)
        self.assertTrue(is_sorted(self.data))

if __name__ == '__main__':
    unittest.main()
