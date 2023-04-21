def draw_plant(plante):
    from ipycanvas import Canvas

    error = False

    displayWidth  = 300
    displayHeight = 300

    canvas = Canvas(width = displayWidth, height = displayHeight)

    # Insert stjålet kode for å tegne her

    if error:
        return False
    else:
        print(plante.name, plante.age)
        display(canvas)