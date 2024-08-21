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

        self.master.geometry("400x300")
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

if __name__ == "__main__":
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()