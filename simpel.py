import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10,10,100)
y = 2*x**2+1000
plt.plot(x, y, '-r', label='y=2x^2+1000')
plt.title('Noah zijn eerste grafiek')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()