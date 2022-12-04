## Exemplul 1

* pentru parole ar trebuie sa se foloseasca **hashing**, nu **encryption**
* presupunand ca ar exista un use case pentru hashing, cheia secreta **nu ar trebui sa apara in source control**(e.g. *git*)

---

## Exemplul 2

* folosirea *hashing*-ului pe username nu ar avea sens, pentru ca oricum acesta ar fi vizibl in aplicatie(e.g. pentru cautare)
* *salt*-ul ar trebui pastrat impreuna cu parola *hash*-uita. motivul este acela ca `gensalt()` va returna mereu ceva random(probabil cu adevarat random), iar nestocarea *salt*-ului generat impreuna cu parola va da rezultate eronate atunci cand, spre exemplu, se va face autentificarea in aplicatie
* `bcrypt.checkpw` nu prea s ar folosi pt usernames

---

## Exemplul 3

* pentru o securitate sporita, ar trebui ca in hash-ul fiecarei parola sa se ia in considerare un salt(care sa fie si stocat)

---

## Exemplul 4

* salt-ul ar trebui sa fie random pentru fiecare parola, nu setat global

---

## Exemplul 5

* nu ar mai trebui sa se foloseasca MD5 pentru stocarea parolelor, nu este safe
