import tkinter as tk
import time

grid_size=5


#w.create_line(x1, y1, x2, y2)



class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        canvas = tk.Canvas(self.root, width=grid_size*50 + 40, height=grid_size*50 + 40)
        canvas.pack()
        #draw a grid
        for i in range(grid_size+1):
            canvas.create_line(50 * i + 20, 20, 50 * i + 20, grid_size*50 + 20)
            canvas.create_line(20, 50 * i + 20, grid_size*50 + 20, 20 + 50 * i)
        self.now=0
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        #now = time.time()
        self.now+=1
        text="Time: "
        text+=str(self.now)
        self.label.configure(text=text)
        self.root.after(1000, self.update_clock)

app=App()

root.mainloop()
