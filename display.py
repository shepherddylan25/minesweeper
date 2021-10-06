class display:
    def __init__(self):
        pass

    def create(self, size):
        import tkinter as tk
        root = tk.Tk()
        for i in range(0,size):
            for f in range(0,size):
                b1 = tk.Button(root, text=('%s %s' % (i, f)), width=0, height=1, command=root.destroy)
                b1.grid(column=i, row=f)
        root.mainloop()
    def dkw(self, size):
        import random
        rows, cols = (size, size)
        arr = [[0 for i in range(cols)] for j in range(rows)]
        for f in range(0,size):
            for n in range(0,size):
                arr[f][n] = (random.getrandbits(1))
        return arr
e = display()
e.create(2)
print(e.dkw(1))
