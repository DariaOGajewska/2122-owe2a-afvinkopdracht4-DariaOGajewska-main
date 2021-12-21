import matplotlib.pyplot as plt
import random
import numpy as np

# for i in range(0,11):
#    n = random.randint(1,100)
#    z.append(n)

def x_and_y(x, y):
    ### OPDRACHT 1 ###
    # Gebruik de lijsten x y en z voor de grafieken van opdracht 1

    plt.plot(x, y)
    plt.title('x tegenover y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def dosis(bestand):
    ### OPDRACHT 2 ###
    '''openen van het bestand'''

    dosis_a =[]
    dosis_b =[]
    open_bestand = open(bestand, 'r')
    regel = open_bestand.readline().strip().split(',')

    for i in open_bestand:
        dosis_a.append(i.strip().split(',')[1])
        dosis_b.append(i.strip().split(',')[2])
    # print(dosis_a)
    # print(dosis_b)

    # Lijndiagram
    # plt.plot(dosis_a, dosis_b)
    # plt.title('dosis a tegenover dosis b')
    # plt.xlabel('Dosis a')
    # plt.ylabel('Dosis b')
    # plt.show()

    # Scatterplot
    # plt.scatter(dosis_a, dosis_b)
    # plt.title('dosis a tegenover dosis b')
    # plt.xlabel('Dosis a')
    # plt.ylabel('Dosis b')
    # plt.show()

    # Hoeveelheid patienten per arts
    janssen = 0
    berends = 0

    open_bestand = open(bestand, 'r')
    for e in open_bestand:
        namen = e.strip().split(',')[3]
        if namen == 'Janssen':
            janssen+=1
        if namen == 'Berends':
            berends+=1
    print('Patienten(Janssen):',janssen)
    print('Patienten(Berends):',berends)
    # Staafdiagram
    # labels = ['P. 1','P. 2','P. 3','P. 4','P. 5','P. 6','P. 7','P. 8','P. 9','P. 10',]
    #
    # x = np.arange(len(labels))  # the label locations
    # width = 0.35  # the width of the bars
    #
    # fig, ax = plt.subplots()
    # rects1 = ax.bar(x - width / 2, dosis_a, width, label='dosis a')
    # rects2 = ax.bar(x + width / 2, dosis_b, width, label='dosis b')
    #
    # # Add some text for labels, title and custom x-axis tick labels, etc.
    # ax.set_ylabel('dosis(mg)')
    # ax.set_title('')
    # ax.set_xticks(x, labels)
    # ax.legend()
    #
    # ax.bar_label(rects1, padding=3)
    # ax.bar_label(rects2, padding=3)
    #
    # fig.tight_layout()
    #
    # plt.show()

    open_bestand.close()

def main():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [3, 6, 8, 10, 12, 12, 4, 14, 7, 10]
    z = []
    #x_and_y(x, y)

    bestand = 'patienten.csv.txt'
    dosis(bestand)

    # Bestand voor opdracht 2
    patienten = "patienten.csv"

    ### OPDRACHT 3 ###
    # Bestand voor opdracht 3
    gist = "yeast_genes.csv"

    ### OPDRACHT 4 ###
    # Bestand voor opdracht 4
    test = "test.csv"

main()