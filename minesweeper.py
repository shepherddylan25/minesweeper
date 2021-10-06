import random

rows, cols = (9, 9)

arr = [[0 for i in range(cols)] for j in range(rows)]
display = [[j for i in range(cols)] for j in range(rows)]

for f in range(0,8):
    for n in range(0,8):
        arr[f][n] = (random.getrandbits(1))

for f in range(1,9):
    for n in range(1,9):
        display[f][n] = "#"

display[0] = [0,"1","2","3","4","5","6","7","8"]

while True:

    for row in display: # This does the displaying
        
        print(row)

    while True:

        try:

            z = list(input("Input Selection 11-88\n"))

            if z == ['s']: # This is just to stop it for now
                break

            z[0] = int(z[0])
            z[1] = int(z[1])

            # If selection is 1-8 continue
            if z[1] and z[0] != 0 and z[0] < 9 and z[1] < 9:
                break

        except:
            print('Try again.')

    if z == ['s']: # This is just to stop it for now
        break

    display[z[0]][z[1]] = str(arr[z[0]][z[1]]) # Update display with arr bit
    print(z)
