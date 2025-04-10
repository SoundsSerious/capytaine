import numpy as np
import capytaine as cpt
import matplotlib.pyplot as plt

cpt.set_logging('INFO')

# Initialize floating body by generating a geometric mesh
mesh = cpt.mesh_horizontal_cylinder(
    length=10.0, radius=1.0,  # Dimensions
    center=(0, 0, -2),        # Position
    resolution=(5, 20, 40)    # Fineness of the mesh
    )
body = cpt.FloatingBody(mesh)

# Define a degree of freedom. The keyword "Heave"
# is recognized by the code and the vertical translation
# motion is automatically defined.
body.add_translation_dof(name="Heave")

# Define the range of water depth
depth_range = list(range(5, 25, 2)) + [np.inf]

# Set up the problems: we will solve a radiation problem for each
# water depth:
problems = [
    cpt.RadiationProblem(body=body, water_depth=depth, omega=2.0)
    for depth in depth_range
]
# Water density, gravity and radiating dof have not been specified.
# Default values are used. (For the radiating dof, the default value
# is usually the first one that has been defined. Here only one has
# been defined.)

# Solve all radiation problems
solver = cpt.BEMSolver()
results = solver.solve_all(problems)

# Gather the computed added mass into a labelled array.
data = cpt.assemble_dataset(results)

# Plot the added mass of each dofs as a function of the water depth.
fig, ax = plt.subplots(layout="constrained")
ax.plot(
    depth_range,
    data['added_mass'].sel(omega=2.0, radiating_dof="Heave", influenced_dof="Heave"),
    marker="s", label="Finite depth"
)
ax.hlines(
    data['added_mass'].sel(omega=2.0, radiating_dof="Heave", influenced_dof="Heave", water_depth=np.inf),
    xmin=20, xmax=30, label="Infinite depth",
    linestyle="--"
)
ax.set(xlabel='Water depth', ylabel='Heave-heave added mass')
ax.legend()
plt.show()
