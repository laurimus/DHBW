import random

def print_tannenbaum(anzahl):
    hoehe = []
    for i in range(anzahl):
        hoehe.append(random.randint(3, 10))
    abstand = max(hoehe) + 2
    stamm_abstand = abstand - 1
    breite = 1
    wald = ''
    for j in range(len(hoehe)):
        for i in range(anzahl):
            for k in range(abstand):wald += '*' if random.random() < 0.1 else ' '       
            wald += 'x' * breite                   
            for k in range(abstand):wald += '*' if random.random() < 0.1 else ' '
        abstand -= 1
        breite += 2 
        wald +='\n' 
    for i in range(anzahl):
        for k in range(stamm_abstand):wald += '*' if random.random() < 0.1 else ' '
        wald += '|_|'
        for k in range(stamm_abstand):wald += '*' if random.random() < 0.1 else ' '
        
    print(wald)
print_tannenbaum(5)

