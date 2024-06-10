# test_sorting.py

import sys
import os
import time
import unittest
from unittest.mock import MagicMock  # Import MagicMock for mocking

# Add the directory containing the 'utils' and 'dicts' modules to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import is_sorted, generate_random_data
from dicts import SORTING_ALGORITHMS_FUNCTIONS, DATASETS

# Mock draw_data function
def draw_data(data, color_array):
    pass  # Mock function, does nothing

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        # Initialize sorting_algorithms dictionary
        self.sorting_algorithms = {}
        for algorithm, function_name in SORTING_ALGORITHMS_FUNCTIONS.items():
            print(algorithm, function_name)
            module = __import__(function_name)
            self.sorting_algorithms[algorithm] = getattr(module, function_name)
        # Open the results file with encoding
        self.results_file = open('tests/results_sorting.txt', 'w', encoding='utf-8')

    def tearDown(self):
        # Close the results file
        self.results_file.close()

    def print_sort_result(self, sort_name, dataset_name, execution_time):
        result = f"{sort_name:<15} - {dataset_name:<20}: Execution Time: {execution_time:.6f} seconds\n"
        print(result)
        self.results_file.write(result)

    def test_sorting_algorithms(self):
        for sort_name, sort_func in self.sorting_algorithms.items():
            header = f"Results for {sort_name}:\n"
            print(header)
            self.results_file.write(header)
            sorted_execution_times = []
            for dataset_name, dataset in DATASETS.items():
                start_time = time.time()
                original_dataset = dataset.copy()
                # Pass a no-op lambda to eliminate delay
                sort_func(dataset, draw_data, 0.01)  # Pass the mock draw_data function
                end_time = time.time()
                execution_time = end_time - start_time
                self.print_sort_result(sort_name, dataset_name, execution_time)
                sorted_execution_times.append((dataset_name, execution_time))
                self.assertTrue(all(dataset[i] <= dataset[i+1] for i in range(len(dataset) - 1)))

            # Sort and display execution times for each dataset
            sorted_execution_times.sort(key=lambda x: x[1])
            sorted_header = f"\nSorted Execution Times for {sort_name}:\n"
            print(sorted_header)
            self.results_file.write(sorted_header)
            for dataset_name, execution_time in sorted_execution_times:
                sorted_result = f"{sort_name} - {dataset_name}: {execution_time:.6f} seconds\n"
                print(sorted_result)
                self.results_file.write(sorted_result)
            print("\n")
            self.results_file.write("\n")

if __name__ == '__main__':
    unittest.main()
