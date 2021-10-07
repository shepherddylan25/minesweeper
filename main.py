import tkinter as tk
import random
def create(size):
    arr = getArr(size)
    root = tk.Tk()

    def test():
        b1.configure(text = '2')
        print(b1)

    for i in range(0,size):

        for f in range(0,size):

            for s in range(0, len(arr)):

                ar = arr[i][f]

                if (ar == 1):
                    b1 = tk.Button(root, text=('#'), width=0, height=1, command=test)
                else:
                    b1 = tk.Button(root, text=('#'), width=0, height=1, command=lambda: print('WINNER'))
                print(b1) # ALSO PRINT TYPE TO TEST IT PLEASE DO THIS THANKS DO THIS NOW YES THANKS
                b1.grid(column=i, row=f)
    
    root.mainloop()
def getArr(size):
    rows, cols = (size, size)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for f in range(0,size):
        for n in range(0,size):
            arr[f][n] = (random.getrandbits(1))
    return arr
create(2)
