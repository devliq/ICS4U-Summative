import time

def insertion_sort(data, update_visualization, speed):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
        update_visualization(data)
        time.sleep(1 / speed())
