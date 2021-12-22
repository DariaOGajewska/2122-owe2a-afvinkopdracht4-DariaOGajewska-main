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
         if e == ['BXZOJU']:
            go = False
         else:
            go = True

   if go == True:
      print('It is a protein sequence')
   else:
      print('It is NOT a protein sequence')

   sequence = ''.join(seq)

   return go, sequence


def check(go, sequence):
   '''Kijkt of een regular expression in de sequentie zit
   input = het bestand
   output = zit de patroon wel/niet in de sequentie
   return = True/False
   '''

   if go == True:
      match = re.search('(MCNSSC)[M|V](GGMNRR)', sequence)
      print('Consensus pattern found:', match.group())
      print('Start of a consensus pattern:', match.start())
      print('End of a consensus pattern:', match.end())
      print('Lenght of a consensus pattern:', (match.end() - match.start()))
   else:
      return False

def main():
   bestand = 'Mus_musculus.GRCm38.pep.all.fa'
   go, sequence = openbestand(bestand)
   check(go, sequence)


main()
