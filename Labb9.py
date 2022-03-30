from LinkedQFile import LinkedQ
from StackFile import Stack


parenteser = Stack()


class Syntaxfel(Exception):
    pass


def readformel(q):
    if not q.isEmpty() and q.peek().isnumeric():
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + str(q))
    readmol(q)
    if not parenteser.isEmpty():
        if q.isEmpty():
            raise Syntaxfel("Saknad högerparentes vid radslutet")
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet " + str(q))


def readmol(q):
    while not q.isEmpty():
        if q.peek() == "(":
            parenteser.push(q.dequeue())
            readmol(q)
        else:
            readgroup(q)


def readgroup(q):
    if not q.isEmpty() and q.peek() == ")":
        if parenteser.isEmpty():
            raise Syntaxfel("Felaktig gruppstart vid radslutet " + str(q))
        q.dequeue()
        if not q.isEmpty() and not q.peek().isnumeric():
            raise Syntaxfel("Saknad siffra vid radslutet " + str(q))
        if q.isEmpty():
            raise Syntaxfel("Saknad siffra vid radslutet")
        parenteser.pop()
    if not q.isEmpty() and q.peek().isalpha():
        readatom(q)
    if not q.isEmpty() and q.peek().isnumeric():
        readNum(q)


def readatom(q):
    atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
                 'K',
                 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
                 'Rb',
                 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
                 'Cs',
                 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf',
                 'Ta',
                 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
                 'Pa',
                 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs',
                 'Mt',
                 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']
    cap = readCap(q)
    atom = cap
    if not q.isEmpty() and q.peek().islower():
        small = readSmall(q)
        atom = cap + small
    if atom not in atoms:
        if q.isEmpty():
            raise Syntaxfel("Okänd atom vid radslutet")
        else:
            raise Syntaxfel("Okänd atom vid radslutet " + str(q))
    if not q.isEmpty() and q.peek().isalpha():
        readatom(q)


def readCap(q):
    """Läser bokstav, dequeue om stor, annars raise Syntaxfel."""
    if not q.isEmpty() and q.peek().isupper():
        return q.dequeue()
    if q.isEmpty():
        raise Syntaxfel("Saknad stor bokstav vid radslutet")
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + str(q))


def readSmall(q):
    """Läser bokstav, dequeue om liten."""
    if not q.isEmpty() and q.peek().islower():
        return q.dequeue()


def readNum(q):
    """Läser nummer för molekyluppsättning av atom, måste vara större än 1, ex H2."""
    if not q.isEmpty() and q.peek() == "0":
        q.dequeue()
        if q.isEmpty():
            raise Syntaxfel("För litet tal vid radslutet")
        raise Syntaxfel("För litet tal vid radslutet " + str(q))
    if not q.isEmpty() and q.peek() == "1":
        q.dequeue()
        if q.isEmpty():
            raise Syntaxfel("För litet tal vid radslutet")
        if not q.isEmpty() and not q.peek().isnumeric():
            raise Syntaxfel("För litet tal vid radslutet " + str(q))
    while not q.isEmpty() and q.peek().isnumeric():
        q.dequeue()


def checkMoleculeSyntax(molecule):
    """Kontrollerar om angiven molekyl följer syntax."""
    q = storeMolecule(molecule)
    while not parenteser.isEmpty():
        parenteser.pop()
    try:
        readformel(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as error:                      # Fångar fel i syntax
        return str(error)                           # Skriver ut  fel


def storeMolecule(molecule):
    """Hjälpfuntion för att lägga in molekylnamn i kö."""
    q = LinkedQ()
    for var in molecule:
        q.enqueue(var)
    return q


def main():
    while True:
        uinput = input()
        if uinput == "#":
            while not parenteser.isEmpty():
                parenteser.pop()
            break
        print(checkMoleculeSyntax(uinput))
        while not parenteser.isEmpty():
            parenteser.pop()


if __name__ == "__main__":
    main()


