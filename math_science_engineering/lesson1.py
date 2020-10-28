# %%

import numpy as np
from skimage import io

img = io.imread('flowers.jpg')
io.imshow(img)

# %%
type(img)

# %%
img.shape

# %%
io.imsave("img_bup.jpg", img)
io.imsave("img_bup.tiff", img)

# %%
img = io.imread('img_bup.tiff')
io.imshow(img)

# %%
