def generate_plant(axiom, rules):
    sentence = axiom

    #The next generation
    finalSentence = ""
        
    for c in sentence:
        #if is F
        if c in rules:             
            finalSentence += rules[c]

        #if is X
        elif c in rules:             
            finalSentence += rules[c]  

        else:
            finalSentence += c
    
    return finalSentence
