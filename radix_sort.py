import time

def radix_sort(data, update_visualization, speed):
    def counting_sort(arr, exp1):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = arr[i] // exp1
            count[(index) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i-1]
        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[(index) % 10] - 1] = arr[i]
            count[(index) % 10] -= 1
            i -= 1
        for i in range(len(arr)):
            arr[i] = output[i]
        update_visualization(arr)
        time.sleep(1 / speed())

    max1 = max(data)
    exp = 1
    while max1 / exp > 1:
        counting_sort(data, exp)
        exp *= 10
