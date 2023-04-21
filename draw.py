from ipycanvas import Canvas
import numpy as np 


displayWidth  = 300
displayHeight = 300

canvas = Canvas(width = displayWidth, height = displayHeight)
canvas.stroke_style = "black"

#testing
string = "FFFFFFFF[+FFFF[+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFF[-FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFFFFFF[-FFFF[+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFF[-FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FFFF[+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFF[-FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X"
x = displayWidth/2
y = displayHeight


angle = 90
length = 10

stack = []

movment = {
    "F": 0,
    "X": 0,
}

direction = {
    "+": 20,
    "-": -20
}

for c in string:

    # change direction of travel
    if c in direction:
        angle += int(direction[c])

    # create line
    elif c in movment:
        move = movment[c]

        # calculate angle
        toRad = int(angle) * (np.pi/180) 

        #next x and y value
        x2 = x - (int(length * np.cos(toRad)))
        y2 = y - length * np.sin(toRad)

        #draw line
        canvas.stroke_line(x, y, x2, y2)

        #change current pos
        x =  x2
        y = y2

    #go back
    elif c == "]":
        goTo = stack[-1]
        x = goTo[0]
        y = goTo[1]
        angle = goTo[2]
        stack.pop()

    #add pos to stack
    elif c == "[":
        stack.append([x,y, angle])

display(canvas)