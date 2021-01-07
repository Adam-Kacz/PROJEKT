# Adam Kaczmarkiewicz 180911
# Projekt zderzenia ciał kulistych

import numpy as np
import matplotlib.pyplot as plt


def kule(masa_1, predkosc_1, promien_1, masa_2, predkosc_2, promien_2):
    global kula1
    global kula2
    kula1 = np.array([masa_1, predkosc_1, promien_1])
    kula2 = np.array([masa_2, -predkosc_2, promien_2])
    return kula1, kula2


def sprezyste(kula_1, kula_2):
    print('Wartosci kul przed zderzeniem [masa predkosc promien]:', kula_1, kula_2)
    nowapredkosc1 = (kula_1[1] * (kula_1[0] - kula_2[0]) + 2 * kula_2[0] * kula_2[1]) / (kula_1[0] + kula_2[0])
    nowapredkosc2 = (kula_2[1] * (kula_2[0] - kula_1[0]) + 2 * kula_1[0] * kula_1[1]) / (kula_1[0] + kula_2[0])
    kula_1[1] = nowapredkosc1
    kula_2[1] = nowapredkosc2
    print('Wartosci kul po zderzeniu [masa predkosc promien]:', kula_1, kula_2)
    return kula_1, kula_2


def nie_sprezyste(kula_1, kula_2):
    print('Wartosci kul przed zderzeniem [masa predkosc promien]:', kula_1, kula_2)
    nowapredkosc1 = (kula_1[1] * kula_1[0] + kula_2[0] * kula_2[1]) / (kula_1[0] + kula_2[0])
    kula_1[1] = nowapredkosc1
    kula_1[0] = kula_1[0] + kula_2[0]
    kula_1[2] = kula_1[2] + kula_2[2]
    print('Wartosci kul po zderzeniu [masa predkosc promien]:', kula_1)
    return kula_1


def wpisz_dane():
    h = 'notfloat'
    while h != float:
        h = input()
        try:
            float(h)
            pass
        except ValueError:
            print('NIE JEST TO LICZBA!\nSPRÓBUJ JESCZE RAZ!\n')
            continue
        else:
            break
    return float(h)


typ = input('Jakie zderzenie chcesz wykonac? Wpisz 1 jako sprezyste lub 2 jako niesprezyste.\n')
while typ != '1' and typ != '2':
    typ = input('SPROBUJ JESZCZE RAZ! Wpisz 1 jako sprezyste lub 2 jako niesprezyste.\n')
if typ == '1':
    print('Wybrano zderzenie sprezyste.\n')
elif typ == '2':
    print('Wybrano zderzenie niesprezyste.\n')

kula1 = np.array([1, 1, 1])
kula2 = np.array([1, 1, 1])

print('Wpisz mase pierwszej kuli:\n')
masa1 = wpisz_dane()
print('Wpisz predkosc pierwszej kuli:\n')
predkosc1 = wpisz_dane()
print('Wpisz promien pierwszej kuli:\n')
promien1 = wpisz_dane()
print('Wpisz mase drugiej kuli:\n')
masa2 = wpisz_dane()
print('Wpisz predkosc drugiej kuli:\n')
predkosc2 = wpisz_dane()
print('Wpisz promien drugiej kuli:\n')
promien2 = wpisz_dane()

kule(masa1, predkosc1, promien1, masa2, predkosc2, promien2)

if kula1[1] > 0:
    zwrot1 = '->'
elif kula1[1] < 0:
    zwrot1 = '<-'
else:
    zwrot1 = ''
if kula2[1] > 0:
    zwrot2 = '->'
elif kula2[1] < 0:
    zwrot2 = '<-'
else:
    zwrot2 = ''

fig, ax = plt.subplots(2)
ax[0].add_patch(plt.Circle((0, 0), promien1, color='r'))
ax[0].add_patch(plt.Circle((promien1*2+promien2*2, 0), promien2, color='g'))

ax[0].text(0, 0, '{} \nM={} \nV={} \nR={}'.format(zwrot1, kula1[0], kula1[1], kula1[2]), va='center', ha='center')
ax[0].text(promien1 * 2 + promien2 * 2, 0, '{} \nm={} \nv={} \nr={}'.format(zwrot2, kula2[0], kula2[1], kula2[2]),
           va='center', ha='center')
ax[0].set_ylabel('Przed zderzeniem')
ax[0].set_aspect('equal', adjustable='datalim')
ax[0].plot()

if typ == '1':
    sprezyste(kula1, kula2)
    if kula1[1] > 0:
        zwrot1 = '->'
    elif kula1[1] < 0:
        zwrot1 = '<-'
    else:
        zwrot1 = ''
    if kula2[1] > 0:
        zwrot2 = '->'
    elif kula2[1] < 0:
        zwrot2 = '<-'
    else:
        zwrot2 = ''
    ax[1].add_patch(plt.Circle((0, 0), promien1, color='r'))
    ax[1].add_patch(plt.Circle((promien1 * 2 + promien2 * 2, 0), promien2, color='g'))

    ax[1].text(0, 0, '{} \nM={} \nV={} \nR={}'.format(zwrot1, kula1[0], kula1[1], kula1[2]), va='center', ha='center')
    ax[1].text(promien1 * 2 + promien2 * 2, 0, '{} \nm={} \nv={} \nr={}'.format(zwrot2, kula2[0], kula2[1], kula2[2]),
               va='center', ha='center')
    ax[1].set_ylabel('Po zderzeniu')
    ax[1].set_aspect('equal', adjustable='datalim')
    ax[1].plot()
elif typ == '2':
    nie_sprezyste(kula1, kula2)
    ax[1].add_patch(plt.Circle((0, 0), kula1[2], color='b'))
    if kula1[1] > 0:
        zwrot1 = '->'
    elif kula1[1] < 0:
        zwrot1 = '<-'
    else:
        zwrot1 = ''
    if kula2[1] > 0:
        zwrot2 = '->'
    elif kula2[1] < 0:
        zwrot2 = '<-'
    else:
        zwrot2 = ''
    ax[1].text(0, 0, '{} \nM={} \nV={} \nR={}'.format(zwrot1, kula1[0], kula1[1], kula1[2]), va='center', ha='center')
    ax[1].set_ylabel('Po zderzeniu')
    ax[1].set_aspect('equal', adjustable='datalim')
    ax[1].plot()
else:
    print('Cos poszlo nie tak :c')

plt.show()
