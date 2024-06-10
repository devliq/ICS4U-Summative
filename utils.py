# utils.py

import random
import time
import json
import csv

def generate_random_data(size, min_value, max_value):
    """Generate a list of random integers."""
    return [random.randint(min_value, max_value) for _ in range(size)]

def generate_sorted_data(size, ascending=True):
    """Generate a sorted list of integers."""
    if ascending:
        return list(range(1, size + 1))
    else:
        return list(range(size, 0, -1))

def generate_reversed_data(size):
    """Generate a list of integers in reversed order."""
    return list(range(size, 0, -1))

def generate_nearly_sorted_data(size, disorder_percentage):
    """Generate a nearly sorted list of integers."""
    sorted_data = list(range(1, size + 1))
    num_disorder = int(size * disorder_percentage)
    disorder_indices = random.sample(range(size), num_disorder)
    for i in disorder_indices:
        sorted_data[i] = random.randint(1, size)
    return sorted_data

def generate_duplicate_values(size, value, num_duplicates):
    """Generate a list with duplicate values."""
    data = [value] * size
    for _ in range(num_duplicates):
        index = random.randint(0, size - 1)
        data[index] = random.randint(1, size)
    return data

def generate_special_case_data(case):
    """Generate special case data."""
    if case == "identical_elements":
        return [1] * 100
    elif case == "two_unique_values":
        return [1, 2] * 50
    elif case == "three_unique_values":
        return [1, 2, 3] * 33
    elif case == "four_unique_values":
        return [1, 2, 3, 4] * 25
    elif case == "five_unique_values":
        return [1, 2, 3, 4, 5] * 20
    else:
        raise ValueError("Invalid special case")

def is_sorted(data):
    """Check if the list is sorted."""
    return all(data[i] <= data[i+1] for i in range(len(data)-1))

def visualize_data(canvas, data):
    """Visualize the data on a given canvas."""
    canvas.delete("all")
    c_width = canvas.winfo_width()
    c_height = canvas.winfo_height()
    x_width = c_width / len(data)
    offset = 10
    spacing = 2
    normalized_data = [i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset
        y0 = c_height - height * c_height
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
    canvas.update()

def read_data_from_txt(filepath):
    """Read data from a .txt file."""
    with open(filepath, 'r') as file:
        return list(map(int, file.readlines()))

def read_data_from_csv(filepath):
    """Read data from a .csv file."""
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        return [int(row[0]) for row in reader]

def read_data_from_json(filepath):
    """Read data from a .json file."""
    with open(filepath, 'r') as file:
        return json.load(file)
