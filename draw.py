def draw(string):
    import numpy as np 

    lines = []

    # Starting point
    x = 5
    y = 5

    # Starting angle
    angle = 90

    # Drawing length 
    length = 10

    # Dictionaries for chars
    movment = {
        "F": 0,
        "X": 0,
    }

    direction = {
        "+": 20,
        "-": -20
    }

    # Stack for branching
    stack = []

    for c in string:

        # Change direction of travel
        if c in direction:
            angle += int(direction[c])

        # Create line
        elif c in movment:
            move = movment[c]

            #  Angle to rad
            toRad = int(angle) * (np.pi/180) 

            # Next x and y value
            x2 = x + (int(length * np.cos(toRad)))
            y2 = y + length * np.sin(toRad)

            # Draw line
            X = [x, x2]
            Y = [y, y2]
            Z = [0, 0]

            lines.append([X,Y,Z])

            # Change current pos
            x =  x2
            y = y2

        # Go back
        elif c == "]":
            goTo = stack[-1]
            x = goTo[0]
            y = goTo[1]
            angle = goTo[2]
            stack.pop()

        # Add pos to stack
        elif c == "[":
            stack.append([x,y, angle])

    return lines

draw("F+-+FF")