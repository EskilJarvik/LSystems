import matplotlib.pyplot as plt
from plant_class import *

plants = [
    plant("test", 0, "(1,0,)F", 22.5, 0, 0, 0, 100),
    plant("wonk", 0, "a", 90, 0, 0, 0, 100),
    plant("fractal", 0, "0", 90, 0, 0, 0, 100),
    plant("plant",0 , "X", 25, 0, 0, 0, 100),
    plant("amogus",      0, "X", 180, 0, 0, 0, 100),
    plant("love",        0, "F", 90, 0, 0, 0, 100),
    plant("Trekant",     0, "F", 120, 0, 0, 0, 100)

]

rulesets = [
    {
        'F': "F[(1,0,&+)F][(1,0,^+)F][(1,0,-^)F][(1,0,&)F]"
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
    }
]

plant_index = int(input("Plant index: "))
start_gen = int(input("Start generation: "))
end_gen = int(input("End generation: "))
 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_box_aspect(aspect=(1, 1, 1))

ax.set_xlim(-25,25)
ax.set_ylim(-25,25)
ax.set_zlim(0,50)

ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Y')

for i in range(end_gen):
    plants[plant_index].grow(rulesets[plant_index])
    if ( i >= start_gen - 1 ):
        plants[plant_index].draw(ax)
plt.show()