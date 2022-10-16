# Metoda Transpozitiei - Double transposition

Metoda transpozitiei presupune rearanajarea pozitiilor caracterelor ce compun *plaintext*-ul.

## Exemplu

Sa spunem ca vrem sa criptam textul *LIFE IS BEAUTIFUL*, iar cheia este *ANDREI*. Cheia va fi aplicata de 2 ori.

Indexam caracterele cheii in functie de ordinea lor alfabetica:

```
1 5 2 6 3 4
A N D R E I
```

Lungimea cheii este 6, deci criptarea ar fi:

```
Pasul 1:

1 5 2 6 3 4
L I F E I S
B E A U T I
F U L X Y Z

LBFFAL ITYSIZ IEUEUX

Pasul 2:

1 5 2 6 3 4
L B F F A L
I T Y S I Z
I E U E U X

LIIFYU AIULZX BTEFSE
```

*X, Y, Z denota valori null.*

Pentru decriptare, se ia textul `LIIFYUAIULZXBTEFSE`, se imparte in string-uri de cate 6(lungimea cheii) si se va ajunge la ceea ce fost detaliat mai sus.

---

## Despre securitate

*Double transposition* este o varianta imbunatatita a lui *Columnar transposition*, iar ideea de baza este aplicarea a doua chei pentru criptare.

Ar putea aparea probleme atunci cand mai multe mesaje de aceeasi lungime sunt criptate cu aceleasi chei.

---

## Cryptoanalysis

Desi se presupunea ca aceasta metoda de criptare este indescifrabila, George Lasry a dovedid contrariul.

---

## Resurse

* [Transposition Cipher](https://en.wikipedia.org/wiki/Transposition_cipher)
* [The Double Transposition Cipher](https://www.pbs.org/wgbh/nova/decoding/doubtrans.html)
* [Double Columnar Transposition](http://www.crypto-it.net/eng/simple/double-transposition.html)