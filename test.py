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
    plant("uno",     0,   "(10,0)F",  22.5,   0, 0, 0,  100), #0
    plant("dos",     0,   "(10,0)F",  25,     0, 0, 0,  100), #1
    plant("tres",    0,   "(7,0)F",   20,     0, 0, 0,  100), #2
]

rulesets = [
    {
        'F': "X[(10,0,&+)F][(10,0,^+)F][(10,0,-^)F][(10,0,&)F]"
    },
    {
        'F': "X[(8,0,&-)F][(9,0,++)F][(10,0,+&)F][(8,0,^-)F]"
    },
    {
        'F': "X[(9,0,^+)F][(10,0,^-)F][(9,0,--)F][(6,0,^)F]"
    }
]

number_of_plants = int(input("Number of plants: "))
end_gen = int(input("Draw gen: "))
generations = end_gen*12

offset = 50
plant_index = 0

plant_array_side_length = math.ceil(number_of_plants**(1/2))
plants = []
for i in range(plant_array_side_length):
    plant_row = []
    for j in range(plant_array_side_length):
        if ( i * plant_array_side_length + j < number_of_plants ):
            plant_row.append( copy_plant(plant_types[plant_index]) )
            plant_row[j].xPos = (i - (plant_array_side_length / 2)) * ( offset + random.randint(offset / -10, offset / 10) )
            plant_row[j].zPos = (j - (plant_array_side_length / 2)) * ( offset + random.randint(offset / -10, offset / 10) )
        else:
            break
    plants.append(plant_row)

waterIntake = [150,150,500,500,500,1000,1000,1000,250,250,250,150]
monthName = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

axis_length = offset * plant_array_side_length

def update(frame):
    i = frame
    ax.cla()
    ax.set_box_aspect(aspect=(1, 1, 1))
    ax.set_xlim(-axis_length/2, axis_length/2)
    ax.set_ylim(-axis_length, axis_length)
    ax.set_zlim(0, axis_length)
    ax.axis('off')
    month = i-12*((i-1)//12)
    ax.text2D(0.4, 0.8, monthName[month-1], transform=ax.transAxes)

    for j in range(plant_array_side_length):
        for k in range(plant_array_side_length):
            if (j * plant_array_side_length + k < number_of_plants ):
                plants[j][k].water = waterIntake[month-1]
                if month not in [12,1,2]:
                    plants[j][k].grow(rulesets[plant_index], month)
                plants[j][k].draw(ax, month)
    
plantAnimation = animation.FuncAnimation(fig, update, frames=range(1, generations + 1), interval=1000, repeat=False)
plt.show()