# radix_sort.py

import time

def radix_sort(data, draw_data, speed):
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)

        for i in range(0, n):
            index = arr[i] // exp
            count[(index) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[(index) % 10] - 1] = arr[i]
            count[(index) % 10] -= 1
            i -= 1

        for i in range(0, len(arr)):
            arr[i] = output[i]

        color_array = ["red" if x == i else "blue" for x in range(len(data))]
        draw_data(data, color_array)
        time.sleep(speed)

    max1 = max(data)
    exp = 1
    while max1 // exp > 0:
        counting_sort(data, exp)
        exp *= 10
