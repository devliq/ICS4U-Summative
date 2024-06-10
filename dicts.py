from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from radix_sort import radix_sort

class SortingMethodsDict:
    methods = {
        "Bubble Sort": bubble_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Heap Sort": heap_sort,
        "Radix Sort": radix_sort,
    }
