import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import random

from plant_class import *

def copy_plant(plant_to_copy):
    copy = plant(plant_to_copy.name, plant_to_copy.age, plant_to_copy.string, plant_to_copy.angle, plant_to_copy.xPos, plant_to_copy.yPos, plant_to_copy.zPos, plant_to_copy.water)
    return copy

plant_types = [
    #     name,     age,   string,    angle,  x, y, z,  water
    plant("test",    0,   "(10,0)F",  22.5,   0, 0, 0,  100), #0
    plant("wonk",    0,   "a",        90,     0, 0, 0,  100), #1
    plant("fractal", 0,   "0",        90,     0, 0, 0,  100), #2
    plant("plant",   0 ,  "X",        25,     0, 0, 0,  100), #3
    plant("amogus",  0,   "X",        180,    0, 0, 0,  100), #4
    plant("love",    0,   "F",        90,     0, 0, 0,  100), #5
    plant("Trekant", 0,   "A",        60,     0, 0, 0,  100)  #6
]

rulesets = [
    {
        'F': "X[(10,0,&+)F][(10,0,^+)F][(10,0,-^)F][(10,0,&)F]"
    },
    {
        'F': ">F<",
        'a': "F[+x]Fb",
        'b': "F[-y]Fa",
        'x': "a",
        'y': "b"
    },
    {
        'F': "FF",
        'X': "F[+X]-X"
    },
    {
        'A': "FXF",
        'B': "XXX"
    },
    {
        'F': "F+F-F-F+F",
    },
    {
        'F': "F-X+F+X-F",
        'X': "XX"
    },
    {
        'F': "F-X+F+X-F",
        'X': "XX"
    }
]

number_of_plants = int(input("Number of plants: "))
plant_index = int(input("Plant index: "))
end_gen = int(input("Draw gen: "))
generations = end_gen*12

offset = 50

plant_array_side_length = math.ceil(number_of_plants**(1/2))
plants = []
for i in range(plant_array_side_length):
    plant_row = []
    for j in range(plant_array_side_length):
        if ( i * plant_array_side_length + j < number_of_plants ):
            plant_row.append( copy_plant(plant_types[plant_index]) )
            plant_row[j].xPos = (i - (i / 2)) * offset + random.randint(offset / -10, offset / 10)
            plant_row[j].zPos = (j - (j / 2)) * offset + random.randint(offset / -10, offset / 10)
        else:
            break
    plants.append(plant_row)

waterIntake = [150,150,600,600,600,1150,1150,1150,250,250,250,150]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

axis_length = offset * plant_array_side_length

def update(frame):
    i = frame
    ax.cla()
    ax.set_box_aspect(aspect=(1, 1, 1))
    ax.set_xlim(-axis_length, axis_length)
    ax.set_ylim(-axis_length, axis_length)
    ax.set_zlim(0, 2 * axis_length)
    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax.set_zlabel('Y')
    month = i-12*((i-1)//12)

    for j in range(plant_array_side_length):
        for k in range(plant_array_side_length):
            if (j * plant_array_side_length + k < number_of_plants ):
                plants[j][k].water = waterIntake[month-1]
                if month not in [12,1,2]:
                    plants[j][k].grow(rulesets[plant_index], month)
                    plants[j][k].draw(ax, month)
    
plantAnimation = animation.FuncAnimation(fig, update, frames=range(1, generations + 1), interval=1000, repeat=False)
plt.show()