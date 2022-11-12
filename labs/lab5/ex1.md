
1. valoarea va fi mereu `0`, deoarece `seed` se *xoreaza* cu el insusi de fiecare data
2. in Python 2, s ar putea ca, de la un punct, `int()` sa returneze aceeasi valoare, deoarece se atinge numarul maxim de tip `int`. in Python 3, **aceasta limita nu mai exista**([sursa](https://note.nkmk.me/en/python-int-max-value/); [sursa](https://stackoverflow.com/a/22948228/9632621)). ce am observat, insa, e ca `int(sys.maxsize + 2)` returneaza `sys.maxsize + 2`, dar tip ul sau este `long`.

```python
# Python 2

import sys

print(sys.maxsize) # 9223372036854775807
print(sys.maxsize + 2) # 9223372036854775809

print(type(9223372036854775809)) # <type 'long'>
print(type(int(9223372036854775809))) # <type 'long'>
```

```python
# Python 3

import sys

print(sys.maxsize) # 9223372036854775807
print(sys.maxsize + 2) # 9223372036854775809

print(type(9223372036854775809)) # <class 'int'>
print(type(int(9223372036854775809)))  # <class 'int'>
```

deci, pare ca in ambele versiuni de Python totul ar merge bine.

3. o singura data va si afisata o valoare; pentru a fi un PRG, trebuie ca `seed` ul urmator sa se bazeze pe valoarea anterior generata; in cazul asta, nici nu se genereaza alte valori si, chiar daca s ar fi generat, tot aceeasi valoare s ar fi *generat* de fiecare data.