# -*- coding: utf-8 -*-
points = 4  # pierwsza liczba jest ukryta
counter = points  # suma punktow
print('Możesz zakończyć sumowanie wpisując 0')
while counter < 21:
    points = input('Wpisz liczbę od 0 do 12: ')
    if points < 0 or points > 12:
        print('Od 0 do 12!')
        continue
    if points == 0:  # kończymy grę
        break
    counter += points  # dodanie liczby
    if counter > 21:  # przegrana
        break
print('Suma=%s' % counter)
