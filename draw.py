def draw_plant(plante):
    from ipycanvas import Canvas

    error = False

    displayWidth  = 300
    displayHeight = 300

    canvas = Canvas(width = displayWidth, height = displayHeight)
    canvas.stroke_style = "black"

    string = plante.string 
    x = 0
    y = 0

    stack = []

    movment = {
        "F": [0,5],
        "X": [0,5],
    }

    angle = {
        "+": 20,
        "-": -20
    }

    for c in string:
        if c in angle:
            angle += int(angle[c])

        elif c in movment:
            move = movment[c]

            # calculate angle

            canvas.stroke_line(x, y, x+move[0], y+move[1])
            x = move[0]
            y = move[1]

        elif c == "[":
            goTo = stack(-1)
            x = goTo[0]
            y = goTo[1]
            angle = goTo[2]
            stack.pop()

        elif c == "[":
            stack.append([x,y, angle])

    if error:
        return False
    else:
        print(plante.name, plante.age)
        display(canvas)