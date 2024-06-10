import time
import random
import tkinter as tk
from ttkbootstrap import Style
from sorting_visualizer import SortingVisualizer
from config import SortingAppConfig
from dicts import SortingMethodsDict
from threading import Thread

class SortingApp:
    def __init__(self, master):
        self.master = master
        self.sorting_methods = SortingMethodsDict.methods
        self.data = []
        self.sorting_in_progress = False

        self.master.title("Sorting Algorithm Visualizer")
        style = Style(theme="cyborg")

        self.canvas = tk.Canvas(width=800, height=400, bg="white")
        self.sorting_visualizer = SortingVisualizer(self.canvas)

        self.selected_algorithm = tk.StringVar(value=list(self.sorting_methods.keys())[0])
        self.speed = tk.IntVar(value=5)

        self.main_frame = tk.Frame(master, padx=10, pady=10)
        self.main_frame.pack(fill="both", expand=True)

        self.create_controls()
        self.create_canvas()
        self.create_algorithm_selection()

    def create_controls(self):
        control_frame = tk.Frame(self.main_frame)
        control_frame.pack(fill="x")

        tk.Button(control_frame, text="Start", command=self.start_sorting, bg="green").pack(side="left")
        tk.Button(control_frame, text="Pause", command=self.pause_sorting, state=tk.DISABLED).pack(side="left")
        tk.Button(control_frame, text="Reset", command=self.reset_sorting).pack(side="left")
        tk.Button(control_frame, text="Exit", command=self.master.quit).pack(side="left")

        tk.Scale(control_frame, from_=1, to=10, orient=tk.HORIZONTAL, label="Speed", variable=self.speed).pack(side="right")

    def create_canvas(self):
        self.canvas.pack(fill="both", expand=True)

    def create_algorithm_selection(self):
        algorithm_frame = tk.Frame(self.main_frame)
        algorithm_frame.pack(fill="x")

        tk.Label(algorithm_frame, text="Select Algorithm:").pack(side="left")
        for algo in self.sorting_methods:
            tk.Radiobutton(algorithm_frame, text=algo, variable=self.selected_algorithm, value=algo).pack(side="left")

    def start_sorting(self):
        self.sorting_in_progress = True
        self.data = [random.randint(1, 100) for _ in range(50)]
        self.sorting_visualizer.draw_data(self.data)
        self.sorting_thread = Thread(target=self.run_sorting)
        self.sorting_thread.start()

    def run_sorting(self):
        method = self.sorting_methods[self.selected_algorithm.get()]
        method(self.data, self.update_visualization, self.speed.get)
        self.sorting_in_progress = False

    def update_visualization(self, data):
        self.sorting_visualizer.draw_data(data)
        time.sleep(1 / self.speed.get())

    def pause_sorting(self):
        self.sorting_in_progress = False

    def reset_sorting(self):
        self.data = []
        self.sorting_visualizer.draw_data(self.data)

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
