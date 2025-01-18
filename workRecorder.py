# Copyright (c) 2025. All rights reserved.
# This software is provided "as-is," without any express or implied warranty.
# In no event will the authors be held liable for any damages arising from the use of this software.
# Permission is granted to anyone to use this software for any purpose, 
# including commercial applications, and to alter it and redistribute it freely, 
# subject to the following restrictions:
# 1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software.
# 2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

import tkinter as tk
from tkinter import ttk
import csv
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        # Set a custom icon
        self.root.iconphoto(False, tk.PhotoImage(file="custom_icon.png"))

        self.start_time = None
        self.timer_running = False

        self.category = tk.StringVar()
        self.type = tk.StringVar()

        # Dropdowns
        self.create_dropdowns()

        # Timer Button
        self.timer_button = tk.Button(self.root, text="Start Timer", command=self.toggle_timer)
        self.timer_button.pack(pady=20)

        # Timer Display
        self.timer_label = tk.Label(self.root, text="Timer: 0:00:00", font=("Helvetica", 14))
        self.timer_label.pack(pady=10)

        # Display recorded data in terminal
        self.console_label = tk.Label(self.root, text="Recorded Data:")
        self.console_label.pack()
        self.console_text = tk.Text(self.root, height=10, state='disabled')
        self.console_text.pack()

        self.output_file = "timer_records.csv"
        self.write_headers()

        self.update_clock()

    def create_dropdowns(self):
        category_label = tk.Label(self.root, text="Choose a category:")
        category_label.pack()
        category_menu = ttk.Combobox(self.root, textvariable=self.category, values=["Story Work", "Story Preparation", "No Story Work"], state="readonly")
        category_menu.pack()
        category_menu.bind("<<ComboboxSelected>>", self.update_background_color)

        type_label = tk.Label(self.root, text="Choose a type:")
        type_label.pack()
        type_menu = ttk.Combobox(self.root, textvariable=self.type, values=["Meeting", "Productive"], state="readonly")
        type_menu.pack()

    def write_headers(self):
        try:
            with open(self.output_file, mode='x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Category", "Type", "Recorded Time (h:m:s)"])
        except FileExistsError:
            pass  # File already exists

    def toggle_timer(self):
        if not self.category.get() or not self.type.get():
            self.show_error("Please select a category and type before starting the timer.")
            return

        if not self.timer_running:
            self.start_timer()
        else:
            self.stop_timer()

    def start_timer(self):
        self.start_time = time.time()
        self.timer_running = True
        self.timer_button.config(text="Stop Timer")

    def stop_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        self.timer_running = False
        self.timer_button.config(text="Start Timer")
        self.record_time(elapsed_time)

    def record_time(self, elapsed_time):
        category = self.category.get()
        type_ = self.type.get()

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{hours}:{minutes:02}:{seconds:02}"

        with open(self.output_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([category, type_, time_str])

        self.update_console(category, type_, time_str)

    def update_console(self, category, type_, time_str):
        self.console_text.config(state='normal')
        self.console_text.insert(tk.END, f"Category: {category}, Type: {type_}, Time: {time_str}\n")
        self.console_text.config(state='disabled')

    def show_error(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_label = tk.Label(error_window, text=message, fg="red")
        error_label.pack(pady=20)
        close_button = tk.Button(error_window, text="Close", command=error_window.destroy)
        close_button.pack()

    def update_background_color(self, event=None):
        category = self.category.get()
        if category == "No Story Work":
            self.root.configure(bg="red")
        elif category == "Story Preparation":
            self.root.configure(bg="yellow")
        elif category == "Story Work":
            self.root.configure(bg="green")
        else:
            self.root.configure(bg="white")

    def update_clock(self):
        if self.timer_running and self.start_time:
            elapsed_time = int(time.time() - self.start_time)
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.timer_label.config(text=f"Timer: {hours}:{minutes:02}:{seconds:02}")
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
