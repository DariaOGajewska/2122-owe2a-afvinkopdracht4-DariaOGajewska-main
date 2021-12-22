import re


def openbestand(bestand):
   '''Opent het bestand en controleert of het een eiwitsequentie is
   input = een bestand
   output = wel/niet eiwit sequentie
   return = het bestand
   '''

   open_bestand = open(bestand, 'r')
   read_from_second_line = open_bestand.readline()

   seq = []

   count = 0
   for regel in open_bestand:
      if count < 5:
         print(regel)
         seq.append(regel)
      count+=1

   sequence = ''.join(seq)

   go = True

   for element in sequence:
      for e in element:
         if e == ['AGTC']:
            go = True
         else:
            go = False

   if go == True:
      print('It is a DNA sequence')
   else:
      print('It is NOT a DNA sequence')


def main():
   bestand = 'Mus_musculus.GRCm38.dna.chromosome.1.fa'
   openbestand(bestand)

main()
