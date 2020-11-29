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


def zderzenia(kula1, kula2):
    print('Wartosci kul przed zderzeniem [masa, predkosc, promien]:', kula1, kula2)
    nowapredkosc1 = (kula1[1] * (kula1[0] - kula2[0]) + 2 * kula2[0] * kula2[1]) / (kula1[0] + kula2[0])
    nowapredkosc2 = (kula2[1] * (kula2[0] - kula1[0]) + 2 * kula1[0] * kula1[1]) / (kula1[0] + kula2[0])
    kula1[1] = nowapredkosc1
    kula2[1] = nowapredkosc2
    print('Wartosci kul po zderzeniu [masa, predkosc, promien]:', kula1, kula2)
    return kula1, kula2


def wpisz_dane():
    x = 'notfloat'
    while x != float:
        x = input()
        try:
            float(x)
            pass
        except ValueError:
            print('NIE JEST TO LICZBA!\nSPRÓBUJ JESCZE RAZ!\n')
            continue
        else:
            break
    return float(x)


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
zderzenia(kula1, kula2)
