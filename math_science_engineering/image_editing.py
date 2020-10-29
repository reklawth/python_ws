# %%
import matplotlib.pyplot as plt

# %%
# 1) Load highrise.jpg into memory
from skimage import io

highrise = io.imread('highrise.jpg')


# %%
# 2) Create a black and white version of highrise.jpg
from skimage.color import rgb2gray

grayscale = rgb2gray(highrise)

fig, ax = plt.subplots(1, 2, figsize=(6, 4))
ax[0].imshow(highrise, cmap=plt.cm.gray)
ax[0].axis('off')
ax[1].imshow(grayscale, cmap=plt.cm.gray)
ax[1].axis('off')

fig.tight_layout()
plt.show

# %%
# 3) Create a version of highrise.jpg with a circular mask on it.
import numpy as np

masked = highrise.copy()

nrows, ncols, nsize = masked.shape
row, col = np.ogrid[:nrows, :ncols]
cnt_row, cnt_col = nrows / 2, ncols /2
outer_disk_mask = (row - cnt_row) ** 2 + (col - cnt_col) ** 2 > (nrows /2 ) ** 2
print(outer_disk_mask)
masked[outer_disk_mask] = 0

fig2, ax2 = plt.subplots(1, 2, figsize=(6, 4))
ax2[0].imshow(highrise, cmap=plt.cm.gray)
ax2[0].axis('off')
ax2[1].imshow(masked, cmap=plt.cm.gray)
ax2[1].axis('off')

fig2.tight_layout()
plt.show

# %%
