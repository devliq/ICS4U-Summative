import time

def bubble_sort(data, update_visualization, speed):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            update_visualization(data)
            time.sleep(1 / speed())