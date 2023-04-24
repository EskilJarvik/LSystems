class plant:
    def __init__ (self, name, age, string):
        self.name = name
        self.age = age
        self.string = string

    def grow(self, ruleset):
        cur_string = self.string
        new_string = ""

        for c in cur_string:
            if c in ruleset:
                new_string += ruleset[c]

        self.string = new_string
        return self
    
    def draw(self):
        import matplotlib.pyplot as plt
        import numpy as np 

        # Set up figure and 3D axes 
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

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

        for c in self.string:

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

                ax.plot(X, Z, Y)

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

        ax.set_xlabel('x')
        ax.set_ylabel('z')
        ax.set_zlabel('y')
        plt.show()
