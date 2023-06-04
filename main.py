import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from plant_class import *

plants = [
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

plant_index = int(input("Plant index: "))
start_gen = int(input("Start generation: "))
end_gen = int(input("End generation: "))
generations = end_gen*12

waterIntake = [150,150,600,600,600,1150,1150,1150,250,250,250,150]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    i = frame
    ax.cla()
    ax.set_box_aspect(aspect=(1, 1, 1))
    ax.set_xlim(-25, 25)
    ax.set_ylim(-25, 25)
    ax.set_zlim(0, 50)
    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax.set_zlabel('Y')
    month = i-12*((i-1)//12)
    plants[plant_index].water = waterIntake[month-1]
    plants[plant_index].grow(rulesets[plant_index],month)
    plants[plant_index].draw(ax)
    
plantAnimation = animation.FuncAnimation(fig, update, frames=range(1, generations + 1), interval=1000, repeat=False)
plt.show()
