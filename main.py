import tkinter as tk
import random
def create(size):
    arr = getArr(size)
    root = tk.Tk()

    def test(i,f):
        print('ee')
    buttons = [[0 for i in range(size)] for j in range(size)]
    for i in range(0,size):

        for f in range(0,size):

            for s in range(0, len(arr)):

                ar = arr[i][f]

                if (ar == 1):
                    b1 = tk.Button(root, text=('#'), width=0, height=1, command=test(i,f))
                else:
                    b1 = tk.Button(root, text=('#'), width=0, height=1, command=lambda: print('b'))
                b1.grid(column=i, row=f)
                
                buttons[i][f] = b1
    
    root.mainloop()
def getArr(size):
    arr = [[0 for i in range(size)] for j in range(size)]
    for f in range(0,size):
        for n in range(0,size):
            arr[f][n] = (random.getrandbits(1))
    return arr
create(4)
