import re

def openbestand(bestand):
   '''Opent het bestand en controleert of het een eiwitsequentie is
   input = een bestand
   output = wel/niet eiwit sequentie
   return = het bestand
   '''

   open_bestand = open(bestand, 'r')
   #read_from_second_line = open_bestand.readline()

   go == False
   for regel in open_bestand:
      for r in regel:
         if r == 'B' or r == 'J' or r == 'O' or r == 'U' or r == 'X' or r == 'Z':
            print('It isn\'t a protein sequence')
            go == False
         else:
            print('It\'s a protein sequence')
            go == True
   return open_bestand, go


def check(open_bestand, go):
   '''Kijkt of een regular expression in de sequentie zit
   input = het bestand
   output = zit de patroon wel/niet in de sequentie
   return = True/False
   '''

   if go == True:
      match = re.search('(MCNSSC)[M|V](GGMNRR)', open_bestand)
      i = (match.group())
      print(i)
   else:
      return False

def main():
   bestand = ''
   openbestand(bestand)
   check(open_bestand, go)

main()