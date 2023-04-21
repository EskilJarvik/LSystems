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
        
        for c in sentence:
            #if is f
            if c == rule1[0]:             
                workingSentence += rule1[1]  
            
            return workingSentence

    #Length of the generation, basically how long it runs
    x = 0
    while x < generations:

        workingSentence = nextGeneration(sentence)    
        sentence = workingSentence
        x += 1
    
    return sentence
print(generate_plant(3))