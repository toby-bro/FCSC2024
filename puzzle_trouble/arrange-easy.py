from PIL import Image
import numpy as np

im = Image.open("puzzle-trouble-easy.jpg")

width, height = im.size

col = 8
row = 8

init_order = []

order = np.array([[74, 56, 13, 73, 17, 41, 62, 25],
                  [45, 70, 20, 14, 57, 46, 26, 40],
                  [42, 51, 35, 67, 43, 66, 12, 63],
                  [61, 47, 10, 27, 15, 1, 24, 6],
                  [37, 5, 4, 21, 64, 50, 55, 71],
                  [7, 32, 33, 2, 77, 0, 23, 76],
                  [52, 60, 65, 53, 22, 75, 16, 31],
                  [44, 54, 34, 72, 36, 3, 11, 30]])

"""
        [22, 41, 1, 54, 50],

        [32, 52, 55, 42, 43],

        [8, 13, 11, 3, 44],

        [30, 23, 49, 48, 39],

        [28, 29, 9, 45, 21],

        [27, 46, 14, 17, 53],

        [12, 18, 24, 35, 34],

        [15, 4, 19, 36, 51],

        [2, 5, 6, 10, 31],

        [26, 47, 7, 20, 16]])
"""

#iorder -= 1 # I started indexing the pieces with 1 instead of 0
def proper(n):
    return n//10*8 + n%10

iorder = proper(order)
#print(iorder)
order = iorder 

for i in range(row):
    for j in range(col):
        piece = im.crop((j*(width/col), i*(height/row), j*(width/col) + (width/col), i*(height/row) + (height/row)))
        init_order.append(piece)

# Get the size of each block

image_width, image_height = init_order[0].size

# Create an empty image to store the final result

final_image = Image.new(mode='RGB', size=(col * image_width, row * image_height))

# Iterate through the array and paste each block into the final image

for r in range(row):
    for c in range(col):
        x = c * image_width
        y = r * image_height
        #print(r,c, order[r,c])
        final_image.paste(init_order[order[r, c]], (x, y))
        #final_image.paste(order[r, c], (x, y))

# Save and show the final image

final_image.save('output.png')
#final_image.show()
