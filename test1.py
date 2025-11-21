import numpy as np
import matplotlib.pyplot as plt

from ray import RayTracer          
from density import SaitoDensity

# -----------------------------------
# 1. Set the frequency of the radio wave
# -----------------------------------
freq = 80e6      # 80 MHz (good for strong coronal refraction)

# -----------------------------------
# 2. Set initial position and direction
# -----------------------------------
# Start at (x,y,z) = (2 Rs, 0, 0)
r0 = np.array([2.0, 0.0, 0.0])

# Shoot ray straight toward the Sun (slightly tilted)
v0 = np.array([-1.0, 0.2, 0])
v0 = v0 / np.linalg.norm(v0)

# -----------------------------------
# 3. Create density model
# -----------------------------------
density_model = SaitoDensity()

# -----------------------------------
# 4. Create the ray tracer
# -----------------------------------
tracer = RayTracer(
    density_model=density_model,
    frequency=freq,
    ds_initial=0.001,
    tol=0.05
)

# -----------------------------------
# 5. Trace the ray
# -----------------------------------
trajectory = tracer.trace(r0, v0, max_steps=5000)

# trajectory is a list of (x,y,z)
trajectory = np.array(trajectory)

# -----------------------------------
# 6. Plot the trajectory
# -----------------------------------
plt.figure(figsize=(6,6))
plt.plot(trajectory[:,0], trajectory[:,2], '-')
plt.xlabel("X (Solar radii)")
plt.ylabel("Z (Solar radii)")
plt.title("Ray trajectory at 80 MHz")
plt.grid(True)
plt.show()
     
