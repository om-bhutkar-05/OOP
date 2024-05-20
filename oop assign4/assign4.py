import tkinter as tk


class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing Application")

        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.start_shape)
        self.canvas.bind("<B1-Motion>", self.draw_shape)
        self.start_x = None
        self.start_y = None
        self.shapes = []

        rectangle_button = tk.Button(self.master, text="Rectangle", command=self.set_rectangle)
        rectangle_button.pack(side=tk.LEFT)
        triangle_button = tk.Button(self.master, text="Triangle", command=self.set_triangle)
        triangle_button.pack(side=tk.LEFT)
        circle_button = tk.Button(self.master, text="Circle", command=self.set_circle)
        circle_button.pack(side=tk.LEFT)

        clear_button = tk.Button(self.master, text="Clear", command=self.clear_canvas)
        clear_button.pack()

    def set_rectangle(self):
        self.current_shape = "rectangle"

    def set_triangle(self):
        self.current_shape = "triangle"

    def set_circle(self):
        self.current_shape = "circle"

    def start_shape(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def draw_shape(self, event):
        if self.start_x is not None and self.start_y is not None:
            x, y = event.x, event.y
            if self.current_shape == "rectangle":
                self.draw_rectangle(x, y)
            elif self.current_shape == "triangle":
                self.draw_triangle(x, y)
            elif self.current_shape == "circle":
                self.draw_circle(x, y)

    def draw_rectangle(self, x, y):
        self.shapes.append(('rectangle', (self.start_x, self.start_y, x, y)))
        self.canvas.create_rectangle(self.start_x, self.start_y, x, y, outline="black", fill="red")

    def draw_triangle(self, x, y):
        x3 = self.start_x + (x - self.start_x) / 2
        y3 = self.start_y
        self.shapes.append(('triangle', (self.start_x, self.start_y, x, y, x3, y3)))
        self.canvas.create_polygon(self.start_x, self.start_y, x, y, x3, y3, outline="black", fill="blue")

    def draw_circle(self, x, y):
        radius = ((x - self.start_x) ** 2 + (y - self.start_y) ** 2) ** 0.5
        self.shapes.append(('circle', (self.start_x, self.start_y, radius)))
        self.canvas.create_oval(self.start_x - radius, self.start_y - radius, self.start_x + radius, self.start_y + radius, outline="black", fill="green")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.shapes = []

def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.geometry("+800+400")
    root.mainloop()

if __name__ == "__main__":
    main()
