def generate_plant(generations):
    import matplotlib.pyplot as plt
    #Define axiom
    axiom = "X"

    #Define the rules

    rule1 = ["F","FF"]
    rule2 = ["X","F-[[X]+X]+F[+FX]-X"]

    sentence = axiom

    #Define the generation
    def nextGeneration(sentence):
        workingSentence = ""
        
        for c in sentence:
            #if is F
            if c == rule1[0]:             
                workingSentence += rule1[1]  

            #if is X
            if c == rule2[0]:             
                workingSentence += rule2[1]  
            
        return workingSentence

    #Length of the generation
    x = 0
    while x < generations:

        workingSentence = nextGeneration(sentence)    
        sentence = workingSentence
        x += 1
    
    return sentence
print(generate_plant(3))