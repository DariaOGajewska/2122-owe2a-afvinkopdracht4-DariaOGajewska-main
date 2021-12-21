from translation import code
from translation import aa3

def opdracht2(dna, strand):
    '''DNA sequentie vertalen naar een eiwit
    input: dna sequentie(str), eiwitten(dictionary)
    output: eiwit sequentie
    '''

    frame1h = 'ATGTAG'
    frame2h = 'ATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAA'
    frame3h = 'ATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAA'

    frame1 = frame1h.lower()
    frame2 = frame2h.lower()
    frame3 = frame3h.lower()

    d = strand.lower()

    if frame1 in d:
        print('frame1 in strand')
    else:
        print('frame1 not in strand')

    if frame2 in d:
        print('frame2 in strand')
    else:
        print('frame2 not in strand')

    if frame3 in d:
        print('frame3 in strand')
    else:
        print('frame3 not in strand')

    eiwit = ''
    eiwit1 = ''
    eiwit2 = ''

    for i in range(0, len(frame1), 3):
        cod = frame1[i:i+3]
        amino = code[cod]
        if amino == '*':
            break
        else:
            eiwit += amino

    print('Eiwitsequentie frame 1:', eiwit)

    for i in range(0, len(frame2), 3):
        cod = frame2[i:i+3]
        amino = code[cod]
        if amino == '*':
            break
        else:
            eiwit1 += amino

    print('Eiwitsequentie frame 2:', eiwit1)

    for i in range(0, len(frame3), 3):
        cod = frame3[i:i+3]
        amino = code[cod]
        if amino == '*':
            break
        else:
            eiwit2 += amino

    print('Eiwitsequentie frame 3:', eiwit2)


def main():
    # Gebruik onderstaande DNA sequentie voor het uitvoeren van
    # opdracht 2 en 3
    dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    strand = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    comp_strand = "TCGGTACATCGATTGAGTCCAATGTACCCCTACTGGGGCGCTGAACCTAATCTCAGAGAAAACCTTATTCGGACTTACTAGGCTCATCGTAGAGTC"

    opdracht2(dna, strand)


main()