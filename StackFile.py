class Node:
    # Hjälpklass, har instansvariabler data och next
    def __init__(self, data, next=None):
        self.data = data    # Någon data
        self.next = next     # För att länka ihop flera Node-objekt

class Stack:
    # Klass för stacken
    # Är alltid tom när man skapar den, ingen fördefinierad instansvariabel
    def __init__(self):
        self.top = None     # Skapar en instansvariabel top som håller reda på toppen av stacken.
                            # Den är tom från början

    def __str__(self):
        tmp = self.top
        items = list()
        while tmp != None:
            items.append(tmp.data)
            tmp = tmp.next
        return "".join(items)


    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.top.data

    #def size(self):

    def push(self, data):
        # Metod för att lägga till ett objekt i stacken. Tar in parameter data.
        # Denna parameter ska innehålla det som ska läggas till i stacken

        tmp = Node(data)    # Anropar Node och skapar ett objekt med data, next sätts till None
                            # Detta objekt ska bli överst i stacken, eftersom det las till senast

        tmp.next = self.top # Det nya objektets next ska peka på den tidigare toppen i listan
                            # eftersom detta nu blir näst överst

        self.top = tmp      # Den nya toppen måste sättas till det nya objekt vi lagt till


    def isEmpty(self):
        # Metod för att kolla om stacken är tom
        return self.top == None

    def pop(self):
        # Metod för att plocka ut det översta objektet i stacken.
        # Behöver ingen parameter, ska returnera ett objekt.
        if self.isEmpty():
            return None
        else:
            tmp = self.top.data     # lagrar datan från det översta Node-objektet, dvs strängen i detta fall
            self.top = self.top.next
            return tmp


#top = Node("adam")   # Variabel som håller reda på Node-objekt. Ska hålla reda på toppen av stacken.
                    # next för denna pekar vidare på det näst översta Node-objektet

#print(top)          # Eftersom vi inte har ngn str-metod ger detta adressen för Node-objektet i ram-minnet
                    # Dvs den plats som variabeln top ska hålla reda på, "pilen" från top till objektet


# Om vi kör koden här så är namnet __main__
# Om vi importerar koden från denna fil till en annan så kommer den få namnet F3 istället för main.

if __name__ == "__main__":  # Denna kod körs endast om vi är inne i denna fil som kontroll för att den fungerar
    s = Stack()
    print(s.isEmpty())
    s.push("ada")
    s.push("beda")
    print("Stack: " + str(s))
    print(s.peek())
    print(s.isEmpty())
    print(s.pop())
    print(s.pop())
    print(s.pop())


