# %%
a = 1
print(a)

# %%

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3*np.pi, 500)
plt.plot(x , np.sin(x**2))
plt.title('Sine wave')
plt.show()
# %%