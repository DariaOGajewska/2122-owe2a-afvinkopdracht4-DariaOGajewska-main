import regex

def check():
   '''Kijkt of een regular expression in de sequentie zit
   input = een bestand
   output = True/False
   '''

   open_bestand = open(bestand)
   #read_from_second_line = open_bestand.readline()
   for regel in open_bestand:
      if [MCNSSC][M|V][GGMNRR] in regel:
         print('Yes')
      else:
         print('-')

def main():

   bestand = ''

main()