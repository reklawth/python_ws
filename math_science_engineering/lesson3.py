# %% 
import numpy as np
from skimage import io

img = io.imread('flowers.jpg')
io.imshow(img)

# %%
img[250][1500]

# %%
for i in range(500):
    for j in range(1000):
       img[i][j][0] = 51 
       img[i][j][1] = 0
       img[i][j][2] = 255
    for k in range(1000, 2000):
       img[i][k][0] = 204 
       img[i][k][1] = 255
       img[i][k][2] = 51
    for l in range(2000, 3000):
       img[i][l][0] = 255 
       img[i][l][1] = 255
       img[i][l][2] = 255

io.imshow(img)

# %%
img = io.imread('flowers.jpg')
io.imshow(img)

# %%
nrows, ncols, nsize = img.shape
row, col = np.ogrid[:nrows, :ncols]
cnt_row, cnt_col = nrows / 2, ncols / 2
outer_disk_mask = ((row - cnt_row)**2 + (col - cnt_col)**2 > (nrows / 2)**2)
img[outer_disk_mask] = 0

io.imshow(img)

# %%
from skimage import color

img = io.imread('flowers.jpg')
io.imshow(img)


# %%
hsv = color.convert_colorspace(img, 'RGB','HSV')
hsv.shape

# %%
hsv[0][0]

# %%
io.imshow(hsv)

# %%
