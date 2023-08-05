#!/usr/bin/env python3
from itertools import count

from more_itertools import partition


def is_positive(value):
    return value >= 0


def main():
    werte = ((-1) ** k / k for k in count(1))

    negative_werte, positive_werte = partition(is_positive, werte)
    ziel = 3.1415
    summe = 0
    for _ in range(1000000):
        summe += next(positive_werte if summe < ziel else negative_werte)
    print(summe)


if __name__ == "__main__":
    main()