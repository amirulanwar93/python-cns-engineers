import numpy as np

l=5 #m
q=20 #kN/m

x = np.linspace(0, l, 20)

M = q / 2 * (l * x - x**2)
V = q * (l / 2 - x)

print(x)
print(M)
print(V)

from matplotlib import pyplot as plt

plt.figure(figsize=(10, 4))
plt.plot([0] * len(x), color="k")
plt.plot(-M)
plt.plot(V)
