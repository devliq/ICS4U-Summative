# insertion_sort.py

import time

def insertion_sort(data, draw_data, speed):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

        color_array = ["red" if x == j+1 or x == i else "blue" for x in range(len(data))]
        draw_data(data, color_array)
        time.sleep(speed)
