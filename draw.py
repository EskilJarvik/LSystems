def draw_plant(plante):
    from ipycanvas import Canvas

    error = False

    displayWidth  = 300
    displayHeight = 300

    canvas = Canvas(width = displayWidth, height = displayHeight)

    string = plante.string 
    x = 0
    y = 0

    movment = {
        "F": [0,5],
        "+": [4,1],
        "-": [-4,1]
    }

    for c in string:
        if c in movment:
            move = movment[c]
            x = move[0]
            y = move[1]

            

    if error:
        return False
    else:
        print(plante.name, plante.age)
        display(canvas)