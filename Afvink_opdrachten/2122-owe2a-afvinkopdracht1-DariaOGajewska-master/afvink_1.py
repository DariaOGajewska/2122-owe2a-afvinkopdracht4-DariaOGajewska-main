def bestandopenen(test_bestand):
    '''Opent het bestand.
    input = bestand - string
    '''

    lijst_1 = []
    lijst_2 = []
    open_bestand = open(test_bestand, 'r')
    regel = open_bestand.readline().strip()
    for r in regel:
        lijst_1.append(r)
    for line in open_bestand:
        for l in line:
            if l != '/n' or l != ' ':
                lijst_2.append(l)
    #print(lijst_2)
    open_bestand.close()

    return lijst_1, lijst_2


def mismatch(lijst_1, lijst_2):
    '''Vergelijkt twee sequenties van een bestand.
    input = bestand - string
    output = mismatches - int
    '''

    mismatches = 0
    for i in range(len(lijst_1)):
        if lijst_1[i] != lijst_2[i]:
            mismatches += 1
    matches = 0
    for i in range(len(lijst_1)):
        if lijst_1[i] == lijst_2[i]:
            matches += 1
    print('Matches:', matches)
    print('Mismatches:', mismatches)
    return mismatches, matches


def main():
    # Lees de twee sequenties in
    # Bereken de hamming distance van deze twee sequenties door ze te
    # vergelijken per positie en de verschillen bij elkaar op te tellen

    #training_bestand = "hamming_distance_training.fa.txt"
    test_bestand = "hamming_distance_test.fa"
    lijst_1, lijst_2 = bestandopenen(test_bestand)
    mismatch(lijst_1, lijst_2)


main()
