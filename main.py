from plant_class import *

plants = [
    plant("test", 0, "F", 22.5, 0, 0, 0, 100),
    plant("wonk", 0, "a", 90, 0, 0, 0, 100),
    plant("fractal", 0, "0", 90, 0, 0, 0, 100)
]

rulesets = [
    {
        'F': "F[&+F]F[^+F][-^F][&F]"
    },
    {
        'F': ">F<",
        'a': "F[+x]Fb",
        'b': "F[-y]Fa",
        'x': "a",
        'y': "b"
    },
    {
        '1': "FF",
        '0': "1[0]0"
    }
]

import matplotlib.pyplot as plt


plant_index = int(input("Plant index: "))
start_gen = int(input("Start generation: "))
end_gen = int(input("End generation: "))

for i in range(end_gen):
    plants[plant_index].grow(rulesets[plant_index])
    if ( i > start_gen ):
        plants[plant_index].draw()
plt.show()