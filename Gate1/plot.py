import numpy as np
import matplotlib.pyplot as plt

# Define the curve |z| = 3
theta = np.linspace(0, 2*np.pi, 100)
r = 3
x = r * np.cos(theta)
y = r * np.sin(theta)

# Define the poles
poles = np.array([0, 1, -2])
pole_markers = ['o', 's', '^']
pole_labels = ['z=0', 'z=1', 'z=-2']

# Plot the curve and poles
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='|z| = 3', color='blue')
for pole, marker, label in zip(poles, pole_markers, pole_labels):
    plt.plot(pole.real, pole.imag, marker, label=label)

plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.title('Curve and Poles')
plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()

