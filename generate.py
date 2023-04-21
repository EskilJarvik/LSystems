def generate_plant(axiom, rule_sets):

    #Define the rules

    rule1 = ["F","FF"]
    rule2 = ["X","F-[[X]+X]+F[+FX]-X"]

    sentence = axiom

    #The next generation
    workingSentence = ""
        
    for c in sentence:
        #if is F
        if c == rule1[0]:             
            workingSentence += rule1[1]  

        #if is X
        if c == rule2[0]:             
            workingSentence += rule2[1]  
    
    return workingSentence

print(generate_plant(3))