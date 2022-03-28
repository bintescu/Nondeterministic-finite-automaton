
class Nod:
    def __init__(self,key):
        self.childs = {}
        self.val = key






nodesVal = []
nodulDeStart = Nod(-1)


def parseFile(filename):
    global nrSimboluri
    global alfabet
    global stareaInitiala
    global stariFinale
    global allNodes
    allNodes = {}
    with(open(filename, 'r')) as f:

        linia1 = f.readline() #comentariu

        linia2 = f.readline() #nr de simboluri
        nrSimboluri = int(linia2)
        print('Nr de simboluri : ',nrSimboluri)

        linia3 = f.readline() #alfabetul
        alfabet = linia3.split()
        print('alfabet : ',alfabet)

        linia4 = f.readline() # starea initiala
        stareaInitiala = linia4.split()[0]
        print('starea initiala :',stareaInitiala)

        linia5 = f.readline() #starile finale
        stariFinale = linia5.split()

        linia6 = f.readline() #numarul de tranzitii
        print('Numar de tranzitii:',linia6)
        # #De aici citim tranzitiile

        for i in range(0,int(linia6)):

            line = f.readline()
            elements = line.split()

            if(len(elements) > 0):
                #Cream nodul
                parinte = elements[0]
                copil = elements[-1]
                ruta = elements[1]

                dictionarulCopilului  = {}
                #Parintele nu se afla in dictionar
                if parinte not in allNodes:
                    allNodes[parinte] = {}
                    allNodes[parinte][copil] = ruta
                #Parintele se afla in dictionar si are deja copilul sub forma de lista deci ii adaugam inca o ruta acelui copil
                elif copil not in allNodes[parinte]:
                    allNodes[parinte][copil] = ruta
                elif isinstance(allNodes[parinte][copil],list):
                    allNodes[parinte][copil].append(ruta)
                #Parintele se afla in dictionar nu are copilul sub forma de lista deci ii facem copilul sub forma de lista
                #Sa ii putem adauga mai multe rute
                else:
                    allNodes[parinte][copil] = [allNodes[parinte][copil],ruta]


def valid1(sirul,nod):
    for a in sirul:
        if a not in alfabet:
            print('Introduceti doar litere care apartin alfabetului')
            return False

    return valid2(sirul,nod)

def valid2(sirul,nod):
    stareLocala = sirul
    #print('Am intrat cu sirul:',sirul,' pe nodul :',nod)
    #Facem toate lamba tranzitiile posibil din acest nod

    if nod in allNodes:
        #print('Cautam copii lui', nod)
        for child in allNodes[nod]:
            if 'L' in allNodes[nod][child]:
                #print('Am gasit o lambda!')
                if valid2(sirul,child):
                    return True
    elif len(sirul) > 0:
        return False

    if len(sirul) > 0:
        simbol = stareLocala[0]
        #print('Am extras simbolul :',simbol)
        for child in allNodes[nod]:
            if simbol in allNodes[nod][child]:
                #print('Am gasit un copil pe care putem merge cu acest simbol',child,' ',allNodes[nod][child],)
                if valid2(stareLocala[1:],child):
                    return True
        #print('Nu exista niciun copil pe care putem merge cu simbolul :',simbol)
        return False
    else:
        if nod in stariFinale:
            #print('Suntem cu sirul vid aici si dam return True')
            return True
        else:
            #print('Suntem cu sirul vid aici si dam return False')
            return False


if __name__ == '__main__':

    parseFile('alDoileaAutomat.txt')
    print(allNodes)



    while True:
        print('Introduceti sirul de caractere:')
        input1 = input()
        if input1 == 'STOP':
            break

        print(valid1(input1, stareaInitiala))


