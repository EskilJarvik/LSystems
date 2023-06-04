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
                while cur_string[i] != ")":
                    characteristics += cur_string[i]
                    i += 1
                characteristics = characteristics.split(",")
                randomAddedLength = float(characteristics[0]) + ( random.randint(1,3) / 10 )
                randomAddedAngle = float(characteristics[1]) + ( random.randint(-2,2) / 10 )
                new_string += f"({randomAddedLength},{randomAddedAngle},{characteristics[2]})"
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

        # Stack for branching
        stack = []

        length = 10
        i = 0

        while i < len(self.string):
            c = self.string[i]

            if c == "(":
                i += 1
                characteristics = ""
                while self.string[i] != ")":
                    characteristics += self.string[i]
                    i += 1
                print(characteristics)
                characteristics = characteristics.split(",")
                length = float(characteristics[0])
                angle = self.angle + float(characteristics[1])
                
                for c in characteristics[2]:
                    if c == "+" or c == "-":
                        if c == "+":
                            rollAngle += float(angle)
                        else:
                            rollAngle -= float(angle)

                    elif c == "^" or c == "&":
                        if c == "^":
                            pitchAngle += float(angle)
                        else:
                            pitchAngle -= float(angle)

            # Create line
            elif c == "F":

                #  Angle to rad
                rollAngleToRad = float(rollAngle) * (np.pi/180)
                pitchAngleToRad = float(pitchAngle) * (np.pi/180) 

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

                i += 1

            # Go back
            elif c == "]":
                newPos = stack.pop()
                x = newPos[0]
                y = newPos[1]
                z = newPos[2]
                rollAngle = newPos[3]
                pitchAngle = newPos[4]
                length = newPos[5]
                i += 1

            # Add pos to stack
            elif c == "[":
                stack.append([x, y, z, rollAngle, pitchAngle, length])
                i += 1

            else: 
                i += 1
