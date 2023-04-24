from draw import *
from plant_class import *

plant_names = [
    "wonk",
    "y"
]

plant_axioms = [
    "a",
    "y"
]

plant_rulesets = [
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

plant_type = int(input("What plant"))
plant = plants(plant_names[plant_type], 0, plant_axioms[plant_type]) 

time = 0
end_time = 3

while time < end_time:
    plant.grow(plant_rulesets[plant_type])
    time = round(time + 0.1)

plant.draw()