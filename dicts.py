# dicts.py

from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from radix_sort import radix_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from quick_sort import quick_sort
from utils import generate_random_data, generate_sorted_data, generate_reversed_data, generate_nearly_sorted_data, generate_duplicate_values, generate_special_case_data

# Dictionary to store sorting algorithm names and their corresponding functions
SORTING_ALGORITHMS = {
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Bubble Sort": bubble_sort,
    "Radix Sort": radix_sort,    
    "Merge Sort": merge_sort, 
    "Heap Sort": heap_sort,
    "Quick Sort": quick_sort
}

SORTING_ALGORITHMS_FUNCTIONS = {
    "Selection Sort": "selection_sort",
    "Insertion Sort": "insertion_sort",
    "Bubble Sort": "bubble_sort",
    "Radix Sort": "radix_sort",    
    "Merge Sort": "merge_sort", 
    "Heap Sort": "heap_sort",
    "Quick Sort": "quick_sort"
}

# Dictionary to store the time complexity of each sorting algorithm
TIME_COMPLEXITIES = {
    "Selection Sort": "O(n^2)",
    "Insertion Sort": "O(n^2)",
    "Bubble Sort": "O(n^2)",
    "Radix Sort": "O(nk)",
    "Merge Sort": "O(n log n)",
    "Heap Sort": "O(n log n)",
    "Quick Sort": "O(n log n)"
}

# Dictionary to store the space complexity of each sorting algorithm
SPACE_COMPLEXITIES = {
    "Selection Sort": "O(1)",
    "Insertion Sort": "O(1)",
    "Bubble Sort": "O(1)",
    "Radix Sort": "O(n + k)",
    "Merge Sort": "O(n)",
    "Heap Sort": "O(1)",
    "Quick Sort": "O(log n)"
}

# Dictionary to store the best case time complexity of each sorting algorithm
BEST_CASE_TIME_COMPLEXITIES = {
    "Selection Sort": "O(n^2)",
    "Insertion Sort": "O(n)",
    "Bubble Sort": "O(n)",
    "Radix Sort": "O(nk)",
    "Merge Sort": "O(n log n)",
    "Heap Sort": "O(n log n)",
    "Quick Sort": "O(n log n)"
}

# Dictionary to store the worst case time complexity of each sorting algorithm
WORST_CASE_TIME_COMPLEXITIES = {
    "Selection Sort": "O(n^2)",
    "Insertion Sort": "O(n^2)",
    "Bubble Sort": "O(n^2)",
    "Radix Sort": "O(nk)",
    "Merge Sort": "O(n log n)",
    "Heap Sort": "O(n log n)",
    "Quick Sort": "O(n^2)"
}

# Dictionary to store the average case time complexity of each sorting algorithm
AVERAGE_CASE_TIME_COMPLEXITIES = {
    "Selection Sort": "O(n^2)",
    "Insertion Sort": "O(n^2)",
    "Bubble Sort": "O(n^2)",
    "Radix Sort": "O(nk)",
    "Merge Sort": "O(n log n)",
    "Heap Sort": "O(n log n)",
    "Quick Sort": "O(n log n)"    
}

# Dictionary to store the stability of each sorting algorithm
STABILITY = {
    "Selection Sort": "Unstable",
    "Insertion Sort": "Stable",
    "Bubble Sort": "Stable",
    "Radix Sort": "Stable",
    "Merge Sort": "Stable",
    "Heap Sort": "Unstable",
    "Quick Sort": "Unstable"
}

# Dictionary to store the score of each sorting algorithm
SCORE = {
    "Selection Sort": "1",
    "Insertion Sort": "2",
    "Bubble Sort": "3",
    "Radix Sort": "4",
    "Merge Sort": "5",
    "Heap Sort": "6",
    "Quick Sort": "7"
}

# Dictionary to store the description of each sorting algorithm
DESCRIPTIONS = {
    "Selection Sort": "Repeatedly finds the minimum element from the unsorted part and puts it at the beginning.",
    "Insertion Sort": "Builds the final sorted array one item at a time.",
    "Bubble Sort": "Repeatedly swaps the adjacent elements if they are in the wrong order.",
    "Radix Sort": "Sorts the numbers by processing individual digits.",
    "Merge Sort": "Divides the array into halves and merges them back in sorted order.",
    "Heap Sort": "Converts the array into a heap and extracts elements in sorted order.",
    "Quick Sort": "Picks an element as pivot and partitions the array around the pivot."
}

# Dictionary to store the pseudocode of each sorting algorithm
PSEUDOCODES = {
    "Selection Sort": [
        "repeat until no unsorted elements:",
        "    find the minimum element in the unsorted part",
        "    swap it with the leftmost unsorted element"
    ],
    "Insertion Sort": [
        "repeat until no unsorted elements:",
        "    take the leftmost unsorted element",
        "    insert it into the correct position in the sorted part"
    ],
    "Bubble Sort": [
        "repeat until no swaps:",
        "    for i from 0 to n-2:",
        "        if i'th and (i+1)'th element are in wrong order:",
        "            swap them"
    ],
    "Radix Sort": [
        "for each digit from least significant to most significant:",
        "    sort the numbers according to that digit"
    ],
    "Merge Sort": [
        "if only one element:",
        "    return",
        "else:",
        "    sort the left half",
        "    sort the right half",
        "    merge the sorted halves"
    ],
    "Heap Sort": [
        "build a max heap from the array",
        "repeat until no elements in the heap:",
        "    extract the maximum element from the heap"
    ],
    "Quick Sort": [
        "if only one element:",
        "    return",
        "else:",
        "    pick a pivot",
        "    partition the array around the pivot",
        "    recursively sort the left and right parts"
    ]
}

# Dictionary to store the flowchart of each sorting algorithm
FLOWCHART = {
    "Selection Sort": "https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif",
    "Insertion Sort": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif",
    "Bubble Sort": "https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif",
    "Radix Sort": "https://upload.wikimedia.org/wikipedia/commons/d/d8/Radix_sort_example.gif",
    "Merge Sort": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif",
    "Heap Sort": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif",
    "Quick Sort": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif"
}

# Dictionary to store the code snippets of each sorting algorithm
CODE_SNIPPETS = {
    "Selection Sort": [
        "def selection_sort(data):",
        "    n = len(data)",
        "    for i in range(n):",
        "        min_idx = i",
        "        for j in range(i+1, n):",
        "            if data[j] < data[min_idx]:",
        "                min_idx = j",
        "        data[i], data[min_idx] = data[min_idx], data[i]"
    ],
    "Insertion Sort": [
        "def insertion_sort(data):",
        "    n = len(data)",
        "    for i in range(1, n):",
        "        key = data[i]",
        "        j = i-1",
        "        while j >= 0 and key < data[j]:",
        "            data[j+1] = data[j]",
        "            j -= 1",
        "        data[j+1] = key"
    ],
    "Bubble Sort": [
        "def bubble_sort(data):",
        "    n = len(data)",
        "    for i in range(n):",
        "        for j in range(0, n-i-1):",
        "            if data[j] > data[j+1]:",
        "                data[j], data[j+1] = data[j+1], data[j]"
    ],
    "Radix Sort": [
        "def counting_sort(data, exp):",
        "    n = len(data)",
        "    output = [0] * n",
        "    count = [0] * 10",
        "    for i in range(n):",
        "        index = data[i] // exp",
        "        count[index % 10] += 1",
        "    for i in range(1, 10):",
        "        count[i] += count[i-1]",
        "    i = n - 1",
        "    while i >= 0:",
        "        index = data[i] // exp",
        "        output[count[index % 10] - 1] = data[i]",
        "        count[index % 10] -= 1",
        "        i -= 1",
        "    for i in range(n):",
        "        data[i] = output[i]",
        "def radix_sort(data):",
        "    max_num = max(data)",
        "    exp = 1",
        "    while max_num // exp > 0:",
        "        counting_sort(data, exp)",
        "        exp *= 10"
    ],
    "Merge Sort": [
        "def merge_sort(data):",
        "    def merge(arr, l, m, r):",
        "        n1 = m - l + 1",
        "        n2 = r - m",
        "        L = arr[l:m+1]",
        "        R = arr[m+1:r+1]",
        "        i = j = 0",
        "        k = l",
        "        while i < n1 and j < n2:",
        "            if L[i] <= R[j]:",
        "                arr[k] = L[i]",
        "                i += 1",
        "            else:",
        "                arr[k] = R[j]",
        "                j += 1",
        "            k += 1",
        "        while i < n1:",
        "            arr[k] = L[i]",
        "            i += 1",
        "            k += 1",
        "        while j < n2:",
        "            arr[k] = R[j]",
        "            j += 1",
        "            k += 1",
        "    def merge_sort_helper(arr, l, r):",
        "        if l < r:",
        "            m = l + (r - l) // 2",
        "            merge_sort_helper(arr, l, m)",
        "            merge_sort_helper(arr, m+1, r)",
        "            merge(arr, l, m, r)",
        "    merge_sort_helper(data, 0, len(data)-1)"
    ],
    "Heap Sort": [
        "def heap_sort(data):",
        "    def heapify(arr, n, i):",
        "        largest = i",
        "        l = 2 * i + 1",
        "        r = 2 * i + 2",
        "        if l < n and arr[l] > arr[largest]:",
        "            largest = l",
        "        if r < n and arr[r] > arr[largest]:",
        "            largest = r",
        "        if largest != i:",
        "            arr[i], arr[largest] = arr[largest], arr[i]",
        "            heapify(arr, n, largest)",
        "    n = len(data)",
        "    for i in range(n // 2 - 1, -1, -1):",
        "        heapify(data, n, i)",
        "    for i in range(n-1, 0, -1):",
        "        data[i], data[0] = data[0], data[i]",
        "        heapify(data, i, 0)"
    ],
    "Quick Sort": [
        "def quick_sort(data):",
        "    def partition(arr, low, high):",
        "        pivot = arr[high]",
        "        i = low - 1",
        "        for j in range(low, high):",
        "            if arr[j] < pivot:",
        "                i += 1",
        "                arr[i], arr[j] = arr[j], arr[i]",
        "        arr[i+1], arr[high] = arr[high], arr[i+1]",
        "        return i+1",
        "    def quick_sort_helper(arr, low, high):",
        "        if low < high:",
        "            pi = partition(arr, low, high)",
        "            quick_sort_helper(arr, low, pi-1)",
        "            quick_sort_helper(arr, pi+1, high)",
        "    quick_sort_helper(data, 0, len(data)-1)"
    ]
}

DATASETS = {
    "Random": generate_random_data(size=100, min_value=1, max_value=1000),
    "Sorted": generate_sorted_data(size=100),
    "Reversed": generate_reversed_data(size=100),
    "Nearly Sorted": generate_nearly_sorted_data(size=100, disorder_percentage=0.1),
    "Duplicate Values": generate_duplicate_values(size=100, value=5, num_duplicates=10),
    "Identical Elements": generate_special_case_data("identical_elements"),
    "Two Unique Values": generate_special_case_data("two_unique_values"),
    "Three Unique Values": generate_special_case_data("three_unique_values"),
    "Four Unique Values": generate_special_case_data("four_unique_values"),
    "Five Unique Values": generate_special_case_data("five_unique_values")
}
