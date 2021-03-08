import sys
import string

pat = ""
text = ""
delta = {}

# citim input-ul si salvam pattern-ul si textul in variabile globale
def readInput():
    file = open(sys.argv[1], "r")
    global pat
    pat = file.readline().strip("\n")
    global text
    text = file.readline().strip("\n")
    file.close()

# functia verifica daca 2 string-uri sunt identice
# nu ma intreba de ce am facut-o, eram moarta de somn pe tren
def match(pattern, string):
    if (len(string) > len(pattern)):
        print("Something's wrong.")
    
    for i in range(len(string)):
        if (pattern[i] != string[i]):
            return False
    
    return True

# verificam care e cel mai lung prefix din text-ul citit care este prefix
# in pattern-ul dat
def prefixMatch(currentString):
    for i in range(len(currentString)):
        if (len(currentString[i:]) > len(pat)):
            index = -len(pat)
        else:
            index = i

        if (match(pat, currentString[index:])):
            return currentString[index:]
    else:
        return ""

# functie ajutatoare, am facut-o initial pentru mine, dar am lasat-o poate
# are cineva nevoie de ea
def printMatrix():
    for i in list(string.ascii_uppercase):
        print(delta[("", i)], end=" ")

    print()
    patt = ""

    for i in pat:
        patt += i
        
        for j in list(string.ascii_uppercase):
            print(delta[patt, j], end=" ")
        
        print()

# aici luam fiecare caz posibil si facem prefix match
def constructMatrix():
    # cazul de baza sa ii zicem asa
    for i in list(string.ascii_uppercase):
        delta[("", i)] = 0
    delta[("", pat[0])] = 1

    # currentText este ce am "citit" pana acum
    currentText = ""
    
    # currentPattern este pattern-ul la care am ajuns cu verificarea
    # mai simplu, linia de matrice pe care o completam
    currentPattern = ""

    for i in pat:
        currentPattern += i

        # luam fiecare caz posibil
        for j in string.ascii_uppercase:
            currentText = currentPattern + j

            # facem longest prefix match
            prefix = prefixMatch(currentText)

            # am gasit un fel de regula matematica cu care sa completez
            # matricea foarte elegant
            delta[(currentPattern, j)] = len(prefix)

def find():
    state = ""
    out = ""

    # aici... doar urmam starile dictate de matrice
    for i in range(len(text)):
        state_nr = delta[(state, text[i])]
        state = pat[:state_nr]
        if state == pat:
            out += str(i - len(pat) + 1)
            out += " "

    out += "\n"
    return out

def writeOutput(str):
    file = open(sys.argv[2], "w")
    file.write(str)
    file.close()

if __name__ == "__main__":
    readInput()
    constructMatrix()
    writeOutput(find())