from plant_class import *

plant_names = [
    "test",
    "wonk",
    "y"
]

plant_axioms = [
    "F",
    "a",
    "y"
]

plant_rulesets = [
    {
        'F': "+F+",
        '+': "FF-",
        '-': "F+"
    },
    {
        'F': ">F<",
        'a': "F[+x]Fb",
        'b': "F[-y]Fa",
        'x': "a",
        'y': "b"
    },
    {
        'X': "X[-FFF][+FFF]FX",
        'Y': "YFX[+Y][-Y]"
    }
]

import matplotlib.pyplot as plt

plant_type = int(input("What plant"))
plants = [plant(plant_names[plant_type], 0, plant_axioms[plant_type], 0, 0, 0)]

gen = 0
end_gen = 3

while gen < end_gen:
    for i in range(len(plants)):
        index = plant_names.index(plants[i].name)
        plants[i].grow(plant_rulesets[index])
    gen += 1
plants[0].draw()
plt.show()
