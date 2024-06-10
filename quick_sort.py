# quick_sort.py

import time

def quick_sort(data, draw_data, speed):
    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)

            color_array = ["red" if x == pi else "blue" for x in range(len(data))]
            draw_data(data, color_array)
            time.sleep(speed)

            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(data, 0, len(data) - 1)
