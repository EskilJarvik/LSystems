import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import time
import random
from plant_class import *


def copy_plant(plant_to_copy):
    copy = plant(plant_to_copy.index,plant_to_copy.name, plant_to_copy.age, plant_to_copy.string, plant_to_copy.angle, plant_to_copy.xPos, plant_to_copy.yPos, plant_to_copy.zPos, plant_to_copy.water)
    return copy


plant_types = [
    #     index name,     age,  string,    angle,  x, y, z,  water
    plant(0,    "uno",    0,   "(10,0)F",  22.5,   0, 0, 0,  100), #0
    plant(1,    "dos",    0,   "(10,0)F",  25,     0, 0, 0,  100), #1
    plant(2,    "tres",   0,   "(7,0)F",   20,     0, 0, 0,  100), #2
]

rulesets = [
    {
        'F': "X[(10,0,&+)F][(10,0,^+)F][(10,0,-)F][(10,0,&)F]"
    },
    {
        'F': "X[(8,0,&-)F][(9,0,++)F][(10,0,+&)F][(8,0,^-)F]"
    },
    {
        'F': "X[(5,0,&+)F][(7,0,--)F][(6,0,^+)F][(8,0,^&-)F]"
    }
]


number_of_plants = int(input("Number of plants: "))
end_gen = int(input("Draw gen: "))
generations = end_gen*12

plant_index = 0

waterIntake = [150,150,550,550,550,1200,1200,1200,250,250,250,150]
monthName = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]


offset = 60
plant_array_side_length = math.ceil(number_of_plants**(1/2))
axis_length = offset * plant_array_side_length
plants = []

for i in range(plant_array_side_length):
    plant_row = []
    for j in range(plant_array_side_length):
        if ( i * plant_array_side_length + j < number_of_plants ):
            plant_row.append( copy_plant(plant_types[plant_index]) )
            plant_row[j].xPos = ((i - (plant_array_side_length / 4)) * offset + random.randint(-10, 10))
            plant_row[j].zPos = ((j - (plant_array_side_length / 4)) * offset + random.randint(-10, 10))
            if plant_index >= len(plant_types)-1:
                plant_index = 0
            else:
                plant_index += 1
        else:
            break
    plants.append(plant_row)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    month = int(frame-12*((frame-1)//12))

    ax.cla()
    ax.set_box_aspect(aspect=(1, 1, 1))
    ax.set_xlim(-axis_length/2, axis_length/2)
    ax.set_ylim(-axis_length/2, axis_length/2)
    ax.set_zlim(0, axis_length)
    ax.axis('off')
    ax.text2D(0.4, 0.85, monthName[month-1], transform=ax.transAxes)

    for j in range(plant_array_side_length):
        for k in range(plant_array_side_length):
            if (j * plant_array_side_length + k < number_of_plants ):
                plants[j][k].water += waterIntake[month-1]
                if month not in [12,1,2]:
                    plants[j][k].grow(rulesets[int(plants[j][k].index)], month)
                plants[j][k].draw(ax, month)

plantAnimation = animation.FuncAnimation(fig, update, frames=range(1, generations + 1), interval=1500, repeat=False)
plt.show()