def generate_plant(generations):
    import matplotlib.pyplot as plt
    #Define axiom
    axiom = "F"

    #Define the rules

    rule1 = ["F","F+F-F-F+F"]

    sentence = axiom

    #Defines
    #F = Gå frem 5
    # - = Snu 90 grader mot klokka
    # + = Snu 90 grader med klokka

    #Define the generation
    def nextGeneration(sentence):
        workingSentence = ""
        xpunkt = 5
        ypunkt = 5
        plt.plot(xpunkt, ypunkt)
        
        plot_x = [xpunkt]
        plot_y = [ypunkt]
        
        directions = ["forward", "right", "backwards", "left"]
        direction = "forward"
        
        for c in sentence:
            #if is f
            if c == rule1[0]:
                if direction == "forward":
                    
                    workingSentence += rule1[1]

                    xpunkt += 0
                    ypunkt += 5
                    
                elif direction == "right":
                    
                    workingSentence += rule1[1]

                    xpunkt += 5
                    ypunkt += 0
                    
                elif direction == "left":
                    
                    workingSentence += rule1[1]

                    xpunkt += -5
                    ypunkt += 0
                    
                else:
                    
                    workingSentence += rule1[1]
                    
                    xpunkt += 0
                    ypunkt -= 5
                
                plot_x.append(xpunkt)
                plot_y.append(ypunkt)

                
            elif c == "-":
                index = directions.index(direction)
                if index == 0:
                    direction = directions[3]
                else:
                    direction = directions[index-1]
                
                
                
            elif c == "+":
                index = directions.index(direction)
                if index == 3:
                    direction = directions[0]
                else:
                    direction = directions[index+1]  

        return workingSentence

    #Length of the generation, basically how long it runs
    x = 0
    while x < generations:

        workingSentence = nextGeneration(sentence)    
        sentence = workingSentence
        x += 1
    
    return sentence
print(generate_plant(3))