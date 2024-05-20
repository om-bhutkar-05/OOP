import tkinter as tk


class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing Application")
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.start_rectangle)
        self.canvas.bind("<B1-Motion>", self.draw_rectangle)
        self.canvas.bind("<Button-3>", self.start_circle)
        self.canvas.bind("<Button-2>", self.start_triangle)
        self.canvas.bind("<B2-Motion>", self.draw_triangle)
        self.canvas.bind("<B3-Motion>", self.draw_circle)
        clear_button = tk.Button(self.master, text="Clear", command=self.clear_canvas)
        clear_button.pack()
        self.start_x = None
        self.start_y = None
        self.shapes = []


    def start_rectangle(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def draw_rectangle(self, event):
        if self.start_x is not None and self.start_y is not None:
            x, y = event.x, event.y
            self.canvas.delete("current_rectangle")
            self.canvas.create_rectangle(self.start_x, self.start_y, x, y, outline="black", fill="red", tags="current_rectangle")
        self.store_shape('rectangle', (self.start_x, self.start_y, x, y, "red"))

    def start_circle(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def draw_circle(self, event):
        if self.start_x is not None and self.start_y is not None:
            x, y = event.x, event.y
            radius = ((x - self.start_x) ** 2 + (y - self.start_y) ** 2) ** 0.5
            self.canvas.delete("current_circle")
            self.canvas.create_oval(self.start_x - radius, self.start_y - radius, self.start_x + radius, self.start_y + radius, outline="black", fill="purple", tags="current_circle")
        self.store_shape('circle', (self.start_x, self.start_y, x, y, "purple"))

    def start_triangle(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def draw_triangle(self, event):
        if self.start_x is not None and self.start_y is not None:
            x, y = event.x, event.y
            x3 = self.start_x + (x - self.start_x) / 2
            y3 = self.start_y
            self.canvas.delete("current_triangle")
            self.canvas.create_polygon(self.start_x, self.start_y, x, y, x3, y3, outline="black", fill="blue", tags="current_triangle")
        self.store_shape('triangle', (self.start_x, self.start_y, x, y, x3, y3, "blue"))




    def store_shape(self, shape_type, coords):
        self.shapes.append({'type': shape_type, 'coords': coords[:-1], 'color': coords[-1]})
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
