def draw_plant(plante):
    from ipycanvas import Canvas

    error = False

    displayWidth  = 300
    displayHeight = 300

    canvas = Canvas(width = displayWidth, height = displayHeight)

    string = plante.string 
    x1 = 0
    y1 = 0

    movment = {
        "F": [0,5],
        "+": [4,1],
        "-": [-4,1]
    }

    for c in string:
        if c in movment:
            move = movment[c]
            x2 = x1 + move[0]
            y2 = y1 + move[1]

            Canvas.stroke_line(x1, y1, x2, y2)

            x1 = x2
            y1 = y2

    if error:
        return False
    else:
        print(plante.name, plante.age)
        display(canvas)