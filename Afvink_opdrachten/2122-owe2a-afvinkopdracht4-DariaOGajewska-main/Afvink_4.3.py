import re

def openbestand(bestand):
   '''Opent het bestand en controleert of het een eiwitsequentie is
   input = een bestand
   output = wel/niet eiwit sequentie
   return = het bestand
   '''

   open_bestand = open(bestand, 'r')
   #read_from_second_line = open_bestand.readline()

   header = []
   seq = []

   go = False
   for regel in open_bestand:
      if regel.startswith('>'):
         header.append(regel)
      else:
         s = regel.strip()
         seq.append(s)

   for element in seq:
      for e in element:
         if e == ['CGAT']:
            go = True
         else:
            go = False

   if go == True:
      print('It is a DNA sequence')
   else:
      print('It is NOT a DNA sequence')

   sequence = ''.join(seq)


def main():
   bestand = 'Mus_musculus.GRCm38.dna.chromosome.1.fa'
   openbestand(bestand)


main()
