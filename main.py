# Adam Kaczmarkiewicz 180911
# Projekt zderzenia ciał kulistych

import numpy as np
import matplotlib.pyplot as plt


def kule(masa1, predkosc1, promien1, masa2, predkosc2, promien2):
    global kula1
    global kula2
    kula1 = np.array([masa1, predkosc1, promien1])
    kula2 = np.array([masa2, predkosc2, promien2])
    return kula1, kula2


def sprezyste(kula1, kula2):
    print('Wartosci kul przed zderzeniem [masa predkosc promien]:', kula1, kula2)
    nowapredkosc1 = (kula1[1] * (kula1[0] - kula2[0]) + 2 * kula2[0] * kula2[1]) / (kula1[0] + kula2[0])
    nowapredkosc2 = (kula2[1] * (kula2[0] - kula1[0]) + 2 * kula1[0] * kula1[1]) / (kula1[0] + kula2[0])
    kula1[1] = nowapredkosc1
    kula2[1] = nowapredkosc2
    print('Wartosci kul po zderzeniu [masa predkosc promien]:', kula1, kula2)
    return kula1, kula2


def nie_sprezyste(kula1, kula2):
    print('Wartosci kul przed zderzeniem [masa predkosc promien]:', kula1, kula2)
    nowapredkosc1 = (kula1[1] * kula1[0] + kula2[0] * kula2[1]) / (kula1[0] + kula2[0])
    kula1[1] = nowapredkosc1
    kula1[0] = kula1[0] + kula2[0]
    kula1[2] = kula1[2] + kula2[2]
    print('Wartosci kul po zderzeniu [masa predkosc promien]:', kula1)
    return kula1


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

etykiety = ['Masa', 'Predoksc', 'Promien']
x = np.arange(len(etykiety))
szerokosc = 0.35

fig, ax = plt.subplots(2)
ax[0].bar(x - szerokosc/2, kula1, szerokosc, label='Kula1')
ax[0].bar(x + szerokosc/2, kula2, szerokosc, label='Kula2')

ax[0].set_ylabel('Wartosci kul przed zderzeniem')
ax[0].set_title('Wartosci kul po zderzeniu [masa predkosc promien]:{} {}'.format(kula1, kula2))
ax[0].set_xticks(x)
ax[0].set_xticklabels(etykiety)
ax[0].legend()

sprezyste(kula1, kula2)

ax[1].bar(x - szerokosc/2, kula1, szerokosc, label='Kula1')
ax[1].bar(x + szerokosc/2, kula2, szerokosc, label='Kula2')

ax[1].set_ylabel('Wartosci kul po zderzeniu')
ax[1].set_title('Wartosci kul po zderzeniu [masa predkosc promien]:{} {}'.format(kula1, kula2))
ax[1].set_xticks(x)
ax[1].set_xticklabels(etykiety)
ax[1].legend()

plt.show()
