import tkinter

grid_size=3

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=grid_size*50 + 40, height=grid_size*50 + 40)
canvas.pack()

#w.create_line(x1, y1, x2, y2)

#draw a grid
for i in range(grid_size+1):
    canvas.create_line(50 * i + 20, 20, 50 * i + 20, grid_size*50 + 20)
    canvas.create_line(20, 50 * i + 20, grid_size*50 + 20, 20 + 50 * i)


root.mainloop()
