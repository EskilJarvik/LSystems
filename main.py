from plant_class import *

plant_names = [
    "test",
    "wonk",
    "fractal"
]

plant_axioms = [
    "F",
    "a",
    "0"
]

plant_rulesets = [
    {
        'F': "FF+[+F-F-F]-[-F+F+F]"
    },
    {
        'F': ">F<",
        'a': "F[+x]Fb",
        'b': "F[-y]Fa",
        'x': "a",
        'y': "b"
    },
    {
        '1': "11",
        'Y': "100"
    }
]

import matplotlib.pyplot as plt

plant_type = int(input("Plant type: "))
plants = [plant(plant_names[plant_type], 0, plant_axioms[plant_type], 20, 0, 0, 0)]

gen = 0
end_gen = int(input("Generations: "))

while gen < end_gen:
    for i in range(len(plants)):
        index = plant_names.index(plants[i].name)
        plants[i].grow(plant_rulesets[index])
    gen += 1

# Set up figure and 3D axes 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_box_aspect(aspect=(1, 1, 1))

ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Y')

plants[0].draw(ax)
plt.show()
