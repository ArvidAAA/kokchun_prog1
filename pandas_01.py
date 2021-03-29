"""Kör filen, funktionen C ritar upp diagramet och använder sig utav 
uppgift/funktion a och b för att få värden till diagramet"""


import matplotlib.pyplot as plt
import pandas

def a():
    df = pandas.read_csv('sysselsättning.csv', header=1, sep=',', usecols=['sysselsättning', 'ålder', 'kön', '2019'])
    sysselsättning = df.loc[df['sysselsättning'] == 'förvärvsarbetande']
    value = sysselsättning['2019'].sum()
    return value
    
def b():
    df = pandas.read_csv('sysselsättning.csv', header=1, sep=',', usecols=['sysselsättning', 'ålder', 'kön', '2019'])
    sysselsättning = df.loc[df['sysselsättning'] == 'ej förvärvsarbetande']
    value = sysselsättning['2019'].sum()
    return value

def c():
    labels = 'förvärvsarbetande', 'Icke förvärvsarbetande'
    sizes = [a(), b()]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

if __name__ == '__main__':
    c()