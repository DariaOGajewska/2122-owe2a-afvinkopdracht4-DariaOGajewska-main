import random

def opdracht_1():
    '''Dictionary'''
    galilean_moons = {'Io': {'Mean radius': 1821.6, 'Surface gravity': 1796, 'Orbital period': 1769},
                      'Europa': {'Mean radius': 1560.8, 'Surface gravity': 1314, 'Orbital period': 3551},
                      'Ganymede': {'Mean radius': 2634.1, 'Surface gravity': 1428, 'Orbital period': 7154},
                      'Callistio': {'Mean radius': 2410.3, 'Surface gravity': 1235, 'Orbital period': 16689}}
    #print(galilean_moons)


def opdracht_5():
    '''Random number(1-10) frequencies'''
    freq = {}
    for i in range(100):
        num = random.randint(1, 10)
        if num in freq.keys():
            freq[num] += 1
        else:
            freq[num] = 1
    print('Frequentie:', freq)


def opdracht_8():
    '''Vegetable prices'''
    vegge = {'tomato': 1.25,
             'potato': 0.85,
             'pepper': 0.99,
             'carrot': 1.45,
             'onion': 2.50}
    a = True
    while a == True:
        print('Menu:', vegge)
        q = input('Do you want to add any changes to your menu? yes/no:')
        if q == 'yes':
            new = input('Add new vegetables, or change the price'
                        '(type the name of the vegetable):')
            if new in vegge.keys():
                vegge[new] = input('Give the price of the vegetable:')
            else:
                price = vegge[new] = input('Give the price of the vegetable:')
                vegge[new] = price
            d = input('Do you want to remove anything? yes/no ')
            if d == 'yes':
                e = input('What do you want to remove?')
                del vegge[e]
            else:
                continue
            a = True
        if q == 'no':
            a = False




    
def main():
    #opdracht_1()
    #opdracht_5()
    opdracht_8()

main()