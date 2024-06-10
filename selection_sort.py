# selection_sort.py

import time

def selection_sort(data, draw_data, speed):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

        color_array = ["red" if x == i or x == min_idx else "blue" for x in range(len(data))]
        draw_data(data, color_array)
        time.sleep(speed)
