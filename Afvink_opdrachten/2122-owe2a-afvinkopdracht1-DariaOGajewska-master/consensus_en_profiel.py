def open_bestand(training_bestand):
    '''opent het bestand'''

    openbestand = open(training_bestand)

    lijst = []
    for i in openbestand:
        if i.startswith('>'):
            continue
        lijst.append(i.rstrip())
    print(lijst)

    A = []
    T = []
    C = []
    G = []
    counter = 0
    for element in lijst:
        for e in element:
            print(e)
            if counter < 1:
                A.append(0)
                T.append(0)
                C.append(0)
                G.append(0)
            indexele = element.index(e)
            if e == 'A':
                A[indexele]+=1
            if e == 'T':
                T[indexele]+=1
            if e == 'C':
                C[indexele]+=1
            if e == 'G':
                G[indexele]+=1
        counter += 1

    print('A:', A)
    print('T:', T)
    print('C:', C)
    print('G:', G)

    consensus = []
    size = len(A)
    for i in range(0, size):
        value = A[i]
        letter = 'A'
        if T[i] > value:
            value = T[i]
            letter = 'T'
        if G[i] > value:
            value = G[i]
            letter = 'G'
        if C[i] > value:
            value = C[i]
            letter = 'C'
        consensus += letter
    print('Consensus:', consensus)


def main():
    training_bestand = "consensus_en_profiel_training.fa"
    test_bestand = "consensus_en_profiel_test.fa"
    open_bestand(training_bestand)

main()