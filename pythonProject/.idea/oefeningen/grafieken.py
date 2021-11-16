import matplotlib.pyplot as plt

def grafiek():
    '''Piechart'''

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:

    labels = ['pizza', 'friet', 'groente', 'taart', 'ijs']
    format = [5, 5, 60, 10, 20]

    fig1, ax1 = plt.subplots()
    ax1.pie(format, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis(
        'equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def diagram():
    '''staafdiagram'''

    import numpy as np

    data = ((3, 1000), (10, 3), (100, 30), (500, 800), (50, 1))

    dim = len(data[0])
    w = 0.75
    dimw = w / dim

    fig, ax = plt.subplots()
    x = np.arange(len(data))
    for i in range(len(data[0])):
        y = [d[i] for d in data]
        b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)

    ax.set_xticks(x + dimw / 2)
    ax.set_xticklabels(map(str, x))
    ax.set_yscale('log')

    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.show()

def lijn(x, y):
    '''lijndiagraam'''

    plt.plot(x, y)
    plt.show()


def main():

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y= [2, 4, 7, 4, 0, 6, 5, 3, 5, 20]
    #z = [2, 8, 21, 16, 0, 36, 35, 24, 45, 200]
    grafiek()
    diagram()
    lijn(x, y)

main()