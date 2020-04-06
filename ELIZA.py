# Julian Grunauer —— 4/3/20 —— Computational Linguistics, Professor Solano —— Dartmouth College 
# This program is a simple chatbot resembling Joseph Weizenbaum's NLP program ELIZA. This chatbot captures input from a Spanish user and mimicks human-sounding responses using ReGex.

import re

print("Hola mi nombre es ELIZA. ¿Cuál es tu nombre?")
while True:
    match_obj = ""
    input1 = input()
     #exit the input loop
    if (input1 == "exit"):
        break

    # ReGex for each of the nine scenarios
    first = re.search(r'(?:Me llamo|Mi nombre es) ([^\.]+)', input1, re.I)
    second = re.search(r'(?P<no>No )?(?:yo estoy|estoy muy|estoy)(?: un poco| bastante| más o menos)? (?P<emotion>[^\.]+)', input1, re.I)
    third = re.search(r'(?P<no>no )?soy (?P<una>una )?(?P<adj>[^\.]+)', input1, re.I)
    fourth = re.search(r'(A mi |Porque mi )(?P<parent>mamá|papá|madre)', input1, re.I)
    fifth = re.search(r'(?P<no>\bno\b )?(?P<quiero>yo quiero|quiero)|(?P<irme> irme)|(?P<debo>debo)|(?P<puedo>yo puedo|puedo)', input1, re.I)
    helper_five = re.search(r'(?P<no>no )?(?P<quiero>yo quiero|quiero)?(?P<irme> irme)?(?P<debo>debo)?(?P<puedo>yo puedo|puedo)? (?P<adj>[^\.]+)', input1, re.I)
    sixth = re.search(r'(?P<pienso>pienso)|(?P<espero>espero)', input1, re.I)
    seventh = re.search(r'(?P<siempre>siempre)', input1, re.I)
    eighth = re.search(r'est.*pid[a|o]|idiota', input1, re.I)
    
    # (1) Initial Greeting
    if (first):
        print("Hola, " + first.group(1) + ". ¿Cómo estás?")

    # (2) State of mind and adverbs      
    elif (second):
        if(second.group('no')):
            print("¿Porqué no estás " + second.group('emotion') +"?")
        else:
            print("¿Porqué estás " + second.group('emotion') +"?")

    # (3) Characteristics of a person (verb soy ‘I am’)
    elif (third):
        if(third.group('no')):
            print("¿Porqué no eres una " + third.group('adj') +"?")
        elif(third.group('una')):
            print("¿Porqué eres una " + third.group('adj') +"?")
        else:
            print("¿Porqué eres " + third.group('adj') +"?")

    # (4) About your family
    elif (fourth):
        print("Cuéntame más de tu " + fourth.group('parent') +"?")
        
    # (5) Handling modal verbs (e.g. poder ‘can’: pued+o ‘I can’ > pued+es ‘you can’) and clitics (V+me>V+te)
    elif (fifth):
        if (helper_five.group('no')):
            if(helper_five.group('irme')):
                print("¿Porqué no quieres irte " + helper_five.group('adj') + "?")
            else:
                print("¿Porqué no quieres " + helper_five.group('adj') + "?")
        elif (helper_five.group('quiero')):
            if(helper_five.group('irme')):
                print("¿Porqué quieres irte " + helper_five.group('adj') + "?")
            else:
                print("¿Porqué quieres " + helper_five.group('adj') + "?")
        elif (helper_five.group('debo')):
            print("¿Porqué debes " + helper_five.group('adj') + "?")
        elif (helper_five.group('puedo')):
            print("¿Porqué puedes " + helper_five.group('adj') + "?")
        else:
            print("error5")

    # (6) Thoughts and hopes (e.g. pensar ‘I think’: piens+o ‘I think’ > piens+as ‘you think’)
    elif (sixth):
        if (sixth.group('espero')):
            print("¿Porqué esperas eso?")
        elif (sixth.group('pienso')):
            print("¿Porqué piensas eso?")
        else:
            print("error2")
    
    # (7) Asking for specific examples
    elif (seventh):
        print("¿Puedes darme un ejemplo específico?")

    # (8) Handling insults
    elif (eighth):
        print("¡Hey, sin insultos! Cálmate y cuéntame más.")

    # (9) All other statements
    else:
        print("Cuéntame más.")






