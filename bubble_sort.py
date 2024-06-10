# bubble_sort.py

import time

def bubble_sort(data, draw_data, speed):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ["green" if x == j or x == j + 1 else "red" for x in range(len(data))])
                time.sleep(speed)
    draw_data(data, ["green" for x in range(len(data))])