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
        import random
        cur_string = self.string
        new_string = ""
        i = 0

        while i < len(cur_string):
            if cur_string[i] in ruleset:
                new_string += ruleset[cur_string[i]]
                i += 1
            elif cur_string[i] == "(":
                i += 1
                characteristics = ""
                while cur_string[i] != "." and cur_string[i] != ")":
                    characteristics += cur_string[i]
                    i += 1
                characteristics = characteristics.split(",")
                randomAddedLength = int(characteristics[0]) + random.randint(1,3)
                new_string += f"({randomAddedLength},{characteristics[1]}"
                while cur_string[i] != ")":
                    new_string += cur_string[i]
                    i += 1
                new_string += cur_string[i]
                i += 1
            else:
                new_string += cur_string[i]
                i += 1
        
        self.string = new_string
        self.age += 1
        return self
    
    def draw(self, ax):
        import matplotlib.pyplot as plt
        import numpy as np 

        # Starting point
        x = self.xPos
        y = self.yPos
        z = self.zPos

        # Angle for rolling or pitcting
        angle = self.angle

        # Starting angle
        rollAngle = 90
        pitchAngle = 90

        # Arrays for chars
        symbos = [["F", "X"], ["+", "-"], ["^", "&"]]

        # Stack for branching
        stack = []

        for c in self.string:

            length = 10

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
                newPos = stack.pop()
                x = newPos[0]
                y = newPos[1]
                z = newPos[2]
                rollAngle = newPos[3]
                pitchAngle = newPos[4]

            # Add pos to stack
            elif c == "[":
                stack.append([x, y, z, rollAngle, pitchAngle])