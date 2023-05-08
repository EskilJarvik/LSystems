class plant:
    def __init__ (self, name, age, string, angle, x, y, z, water):
        self.name = name
        self.age = age
        self.string = string
        self.angle = angle
        self.xPos = x
        self.yPos = y
        self.zPos = z
        self.water = water

    def grow(self, ruleset):
        cur_string = self.string
        new_string = ""

        for c in cur_string:
            if c in ruleset:
                new_string += ruleset[c]
            else:
                new_string += c

        self.string = new_string
        return self
    
    def draw(self):
        import matplotlib.pyplot as plt
        import numpy as np 

        # Set up figure and 3D axes 
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.set_box_aspect(aspect=(1, 1, 1))

        ax.set_xlabel('X')
        ax.set_ylabel('Z')
        ax.set_zlabel('Y')

        # Starting point
        x = self.xPos
        y = self.yPos
        z = self.zPos

        # Angle for rolling or pitcting
        angle = self.angle

        # Starting angle
        rollAngle = 90
        pitchAngle = 90

        # Drawing length 
        length = 10

        # Arrays for chars
        symbos = [["F", "X"], ["+", "-"], ["^", "&"]]

        # Stack for branching
        stack = []

        for c in self.string:

            # Change direction of travel
            if c in symbos[1]:
                if c == symbos[1][0]:
                    rollAngle += int(angle)
                else:
                    rollAngle -= int(angle)

            elif c in symbos[2]:
                if c == symbos[2][0]:
                    pitchAngle += int(angle)
                else:
                    pitchAngle -= int(angle)

            # Create line
            elif c in symbos[0]:

                #  Angle to rad
                rollAngleToRad = int(rollAngle) * (np.pi/180)
                pitchAngleToRad = int(pitchAngle) * (np.pi/180) 

                # Next x and y value
                x2 = x + int(length * np.cos(rollAngleToRad))
                y2 = y + length * np.sin(rollAngleToRad)
                z2 = z + int(length * np.cos(pitchAngleToRad))

                # Draw line
                X = [x, x2]
                Y = [y, y2]
                Z = [z, z2]

                ax.plot(X, Z, Y, color ='black')

                # Change current pos
                x =  x2
                y = y2
                z = z2

            # Go back
            elif c == "]":
                newPos = stack[-1]
                x = newPos[0]
                y = newPos[1]
                z = newPos[2]
                rollAngle = newPos[3]
                pitchAngle = newPos[4]
                stack.pop()

            # Add pos to stack
            elif c == "[":
                stack.append([x, y, z, rollAngle, pitchAngle])
                
        plt.show()