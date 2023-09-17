import matplotlib.pyplot as plt
import numpy as np

# Početni uvjeti
g = 9.81  # Gravitacijsko ubrzanje (m/s^2)
initial_height = 1000  # Početna visina objekta (metri)
initial_velocity = 0  # Početna brzina objekta (m/s)
time_step = 0.01  # Vremenski korak (sekunde)
num_steps = 1000  # Broj koraka simulacije

# Inicijalizacija
time = np.arange(0, num_steps * time_step, time_step)
height = np.zeros(num_steps)
velocity = np.zeros(num_steps)

height[0] = initial_height
velocity[0] = initial_velocity

# Simulacija slobodnog pada
for step in range(1, num_steps):
    velocity[step] = velocity[step - 1] + g * time_step
    height[step] = height[step - 1] - velocity[step - 1] * time_step

# Vizualizacija
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, height)
plt.title('Visina objekta tijekom vremena')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Visina (m)')

plt.subplot(2, 1, 2)
plt.plot(time, velocity)
plt.title('Brzina objekta tijekom vremena')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Brzina (m/s)')

plt.tight_layout()
plt.show()
