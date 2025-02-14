import tkinter
from tkinter import ttk
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from logging import getLogger

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.master.geometry("400x400")
        self.master.title("test")

        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tkinter.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there.bind("<Button-1>", self.call_wait)
        self.hi_there.place(x=20, y=20)
        self.hi_there.pack()

        self.progressbar = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.progressbar.place(x=20, y=50)
        self.progressbar.pack()
        self.progressbar.configure(maximum=100, value=0)

        self.ground_x_label = tkinter.Label(self, text="x座標")
        self.ground_x_label.place(x=20, y=80)
        self.ground_x_label.pack()

        self.ground_x_entry = tkinter.Entry(self, width=10)
        self.ground_x_entry.place(x=40, y=80)
        self.ground_x_entry.pack()

        self.ground_y_label = tkinter.Label(self, text="y座標")
        self.ground_y_label.place(x=20, y=110)
        self.ground_y_label.pack()

        self.ground_y_entry = tkinter.Entry(self, width=10)
        self.ground_y_entry.place(x=40, y=110)
        self.ground_y_entry.pack()

        self.target_x_label = tkinter.Label(self, text="x座標")
        self.target_x_label.place(x=20, y=140)
        self.target_x_label.pack()

        self.target_x_entry = tkinter.Entry(self, width=10)
        self.target_x_entry.place(x=40, y=140)
        self.target_x_entry.pack()

        self.target_y_label = tkinter.Label(self, text="y座標")
        self.target_y_label.place(x=20, y=170)
        self.target_y_label.pack()

        self.target_y_entry = tkinter.Entry(self, width=10)
        self.target_y_entry.place(x=40, y=170)
        self.target_y_entry.pack()

        self.calc_distance_button = tkinter.Button(self)
        self.calc_distance_button["text"] = "距離計算"
        self.calc_distance_button.bind("<Button-1>", self.calc_distance)
        self.calc_distance_button.place(x=20, y=220)
        self.calc_distance_button.pack()

        self.output = tkinter.Label(self, text="")
        self.output.place(x=20, y=270)
        self.output.pack()

    def call_wait(self, event):
        self.hi_there.config(state=tkinter.DISABLED)
        self.progressbar.configure(value=0)
        thread1 = threading.Thread(target=self.wait(sec=3))
        thread1.start()

    def wait(self, sec):
        print(f"wait {sec} seconds")
        for i in range(sec):
            time.sleep(1)
            self.progressbar.configure(value=(i+1)*100/3)
        print("waited 3 seconds")
        self.hi_there.config(state=tkinter.NORMAL)

    def calc_distance(self, x1, y1, x2, y2):
        x1 = int(self.ground_x_entry.get())
        y1 = int(self.ground_y_entry.get())
        x2 = int(self.target_x_entry.get())
        y2 = int(self.target_y_entry.get())
        distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
        self.output["text"] = f"距離: {distance}\n{distance/100}um"

if __name__ == "__main__":
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()