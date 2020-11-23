# Adam Kaczmarkiewicz 180911
# Projekt zderzenia ciał kulistych

import numpy as np
import matplotlib.pyplot as plt


def kule(masa1, predkosc1, promien1, masa2, predkosc2, promien2):
    global kula1
    global kula2
    kula1 = np.array([float(masa1), predkosc1, promien1])
    kula2 = np.array([float(masa2), predkosc2, promien2])
    return kula1, kula2


def zderzenia(kula1, kula2):
    print('Wartosci kul przed zderzeniem [masa, predkosc, promien]:', kula1, kula2)
    nowapredkosc1 = (kula1[1] * (kula1[0] - kula2[0]) + 2 * kula2[0] * kula2[1]) / (kula1[0] + kula2[0])
    nowapredkosc2 = (kula2[1] * (kula2[0] - kula1[0]) + 2 * kula1[0] * kula1[1]) / (kula1[0] + kula2[0])
    kula1[1] = nowapredkosc1
    kula2[1] = nowapredkosc2
    print('Wartosci kul po zderzeniu [masa, predkosc, promien]:', kula1, kula2)

    return kula1, kula2


kule(1, 2, 1, 1, 1, 1)
zderzenia(kula1, kula2)
