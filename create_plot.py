import numpy as np

import matplotlib.pyplot as plt


import tikzplotlib as tzl

n = [1,2,3]
x = np.arange(-3.1415296,3.1415296,.1)

for i in n:
    y = np.cos(i*x)
    plt.plot(x,y)
tzl.save("plot_out.tex")
