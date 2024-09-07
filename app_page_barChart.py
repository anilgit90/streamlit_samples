import matplotlib.pyplot as plt
import numpy as np

# Does not work due to matplotlib.pyplot library error
s = np.random.logistic(10,5,size=5)
chart,ax = plt.subplots()
ax.hist(s,bins=15)

"chart",chart