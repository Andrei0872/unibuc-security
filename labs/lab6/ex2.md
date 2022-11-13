> Executați secvența de mai sus. Ce obțineți?

Secventa de mai sus cripteaza simetric textul stocat in variabila `data` folosind cheia `key`. 

> Ce mod de operare este folosit? Ce observați?

Modul de criptare este ECB(Electronic Code Block).

Observ ca cifrul de tip ECB se creeaza inca de la inceput, o singura data, prin `new()`. Apoi, pe noul obiect creat, se pot apela metode de genul `encrypt()` sau `decrypt()`.

```python
print(result)
print(cipher.decrypt(result))
```

> Ați recomanda folosirea modului de operare de la b)? De ce? De ce nu?

Nu s ar recomanda folosirea sa deoarece **nu este sigur din punct de vedere semantic**, ceea ce inseamna ca din *ciphertext* se pot extrage date ne-neglijabile despre textul initial([sursa](https://en.wikipedia.org/wiki/Semantic_security)). Acest lucru se poate intampla deoarece acelasi text va fi mereu criptat in acelasi *ciphertext*([sursa](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation)).

Motivele pentru care acest mod s ar folosi pot fi strict didactice.

> Care este dimensiunea cheii? Dar a blocului?

```python
print(len(data)) # 48
print(len(key)) # 16
```

Se observa ca ambele lungimi sunt multipli de 16. 16 este, totodata, dimensiunea in bytes a blocului cu care lucreaza AES.

> Modificați codul astfel încât să funcționeze dacă se înlocuiește valoarea data cu data=b'test'.

```python
data = b'test'
data = Padding.pad(data, 16)

cipher = AES.new(key, AES.MODE_ECB)
result = cipher.encrypt(data)

print(result)
print(cipher.decrypt(result))
```

> Refaceți codul, schimbând modul de operare cu un alt mod de operare pe care îl considerați mai potrivit.


```python
header = b'header or associated data - not encrypted!'
data = b'nobody needs to know this!!'
key = Padding.pad(b'nobody would guess this', 16)

cipher = AES.new(key, AES.MODE_EAX)
cipher.update(header)

ciphertext, tag = cipher.encrypt_and_digest(data)

print(ciphertext)
```

Am ales modul [EAX](https://en.wikipedia.org/wiki/EAX_mode) deoarece acesta vine la pachet nu numai cu *privacy*, dar si cu *autentificare*.