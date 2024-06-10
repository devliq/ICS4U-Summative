# main.py

import sys
import os
import time
import random
from threading import Thread
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from config import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE
from utils import generate_random_data, visualize_data
from dicts import SORTING_ALGORITHMS

class SortingApp:
    def __init__(self, master):
        self.master = master
        self.main_frame = None

        self.sorting_methods = SORTING_ALGORITHMS
        self.root = self.master
        self.data = []
        self.root.title("Sorting Algorithm Visualizer")
        
        style = Style(theme="cyborg")

        self.canvas = tk.Canvas(width=800, height=400, bg="white")
        self.sorting_in_progress = False

        self.main_frame = tk.Frame(root, padx=10, pady=10)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.create_control_buttons()
        self.create_speed_controls()
        self.create_algorithm_selection()
        self.create_canvas()
        self.configure_grid(self.main_frame, rows=3, cols=2)
        self.selected_algorithm = None

    def configure_grid(self, frame, rows, cols):
        for i in range(rows):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols):
            frame.grid_columnconfigure(j, weight=1)

    def create_control_buttons(self):
        control_frame = tk.LabelFrame(self.main_frame, text="Controls")
        control_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        buttons = [
            ("Start", self.start_stop_sorting, "green"),
            ("Pause", self.pause_sorting, tk.DISABLED),
            ("Step", self.step_sorting, tk.DISABLED),
            ("Reset", self.reset_sorting, "lightgray"),
            ("Exit", self.master.quit)
        ]

        for text, command, *button_props in buttons:
            color, state = button_props if len(button_props) == 2 else ("lightgray", tk.NORMAL)
            button = tk.Button(control_frame, text=text, bg=color, command=command, state=state)
            button.pack(side="left", padx=5, pady=5)
            if text == "Pause":
                self.pause_button = button
            elif text == "Step":
                self.step_button = button
            elif text == "Start":
                self.start_button = button

    def create_speed_controls(self):
        speed_frame = tk.LabelFrame(self.main_frame, text="Speed Controls")
        speed_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.speed_scale = tk.Scale(speed_frame, from_=1, to=10, orient=tk.HORIZONTAL, label="Speed")
        self.speed_scale.pack(side="left", padx=5, pady=5)

    def create_algorithm_selection(self):
        algorithm_frame = tk.LabelFrame(self.main_frame, text="Select Algorithm")
        algorithm_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.selection_notebook = ttk.Notebook(algorithm_frame)
        self.selection_notebook.grid(row=0, column=0, sticky="nsew")

        algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Heap Sort"]
        random_algorithm = random.choice(algorithms)

        for algo in algorithms:
            frame = tk.Frame(self.selection_notebook)
            self.selection_notebook.add(frame, text=algo)
            ttk.Label(frame, text="Algorithm Description:").grid(row=0, column=0, padx=5, pady=(10, 0), sticky="w")
            ttk.Label(frame, text=self.get_algorithm_description(algo)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
            ttk.Label(frame, text="Algorithm Comparison:").grid(row=2, column=0, padx=5, pady=(10, 0), sticky="w")

            radio_var = tk.IntVar(value=algo == random_algorithm)
            radiobutton = ttk.Radiobutton(frame, text="Select", variable=radio_var, command=lambda a=algo: self.set_selected_algorithm(a))
            radiobutton.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.selected_algorithm_var = tk.StringVar(value=random_algorithm)
        self.selection_notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)

    def on_tab_changed(self, event):
        selected_tab = self.selection_notebook.tab(self.selection_notebook.select(), "text")
        self.set_selected_algorithm(selected_tab)

    def set_selected_algorithm(self, algorithm):
        self.selected_algorithm_var.set(algorithm)
        self.selected_algorithm = algorithm

    def create_canvas(self):
        canvas_frame = tk.LabelFrame(self.main_frame, text="Visualization")
        canvas_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.canvas = tk.Canvas(canvas_frame, width=800, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def start_stop_sorting(self):
        if not self.sorting_in_progress:
            self.sorting_in_progress = True
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.step_button.config(state=tk.NORMAL)

            self.data = [random.randint(1, 100) for _ in range(50)]
            self.draw_data(self.data, ["red" for _ in range(len(self.data))])

            sorting_thread = Thread(target=self.run_sorting_algorithm)
            sorting_thread.start()
        else:
            self.sorting_in_progress = False

    def pause_sorting(self):
        self.sorting_in_progress = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.step_button.config(state=tk.DISABLED)

    def step_sorting(self):
        pass  # Implement step sorting if needed

    def reset_sorting(self):
        self.sorting_in_progress = False
        self.data = []
        self.canvas.delete("all")

        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.step_button.config(state=tk.DISABLED)

    def run_sorting_algorithm(self):
        algorithm = self.sorting_methods[self.selected_algorithm]
        speed = 0.1 / self.speed_scale.get()
        algorithm(self.data, self.draw_data, speed)

        self.sorting_in_progress = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.step_button.config(state=tk.DISABLED)

    def draw_data(self, data, color_array):
        self.canvas.delete("all")
        canvas_height = 400
        canvas_width = 800
        bar_width = canvas_width / (len(data) + 1)
        offset = 10
        spacing = 2
        normalized_data = [i / max(data) for i in data]

        for i, height in enumerate(normalized_data):
            x0 = i * bar_width + offset + spacing
            y0 = canvas_height - height * 390
            x1 = (i + 1) * bar_width + offset
            y1 = canvas_height

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])

        self.master.update_idletasks()

    def get_algorithm_description(self, algo):
        descriptions = {
            "Bubble Sort": "Repeatedly swaps the adjacent elements if they are in the wrong order.",
            "Selection Sort": "Repeatedly finds the minimum element from the unsorted part and puts it at the beginning.",
            "Insertion Sort": "Builds the final sorted array one item at a time.",
            "Merge Sort": "Divides the array into halves and merges them back in sorted order.",
            "Quick Sort": "Picks an element as pivot and partitions the array around the pivot.",
            "Radix Sort": "Sorts the numbers by processing individual digits.",
            "Heap Sort": "Converts the array into a heap and extracts elements in sorted order."
        }
        return descriptions.get(algo, "No description available.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
