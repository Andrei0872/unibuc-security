## Exemplul 1 - stocarea de *sensitive data* in LocalStorage

Din moment ce `LocalStorage` poate fi accesat prin JavaScript, un mediu care nu a trecut prin procesul de [*HTML sanitization*](https://en.wikipedia.org/wiki/HTML_sanitization) reprezinta prima usa deschisa spre XSS.

**O prima masura** de combatere a acestui risc este folosirea unui framework care se asigura ca ceea ce pune in DOM este XSS-safe.

Cu toate acestea, asta **nu este suficient**. In ziua de azi, se folosesc tot felul de biblioteci, iar codul lor ajunge sa fie parte din ceea ce este procesat de browser-ul user-ului. Asta inseamna ca un atacator poate **efectua un atac XSS** si prin injectarea de cod malitios intr-o biblioteca.

**O masura** si pentru asta o constitui nefolosirea `LocalStorage`-ului pentru a stoca sensitive data, cum ar un JWT sau un refresh token.

---

## Exemplul 2 - validarea de rolui doar pe front end

Pentru aplicatii in care exista mai multe roluri, exista framework-uri de front end care permit protejarea rutelor cu usurinta.

Cu toate astea, securitatea pe front end este doar un *zid de hartie*. Adevarata protectie trebuie sa aiba loc pe back end. Altfel, un atacator poate observa in ce mod se trimite request-ul spre server pentru un admin, iar acesta poate sa efectua aceeasi operatie dintr-un terminal(e.g. folosind `curl`) sau chiar din consola browser-ului.

**Solutia**, in acest caz, este asigurarea ca rutele sunt protejate nu doar pe front end, dar si (mai ales) pe back end.

---

## Exemplul 3 - Folosirea de cookies fara cu policy `None` si fara CSRF token

CSRF este un atac prin care atacatorul efectueaza actiuni din partea user-ului, fara ca user-ul sa isi dea seama sau sa fie de acord.

Intr-un cookie se poate tine ID-ul sesiunii user-ului, ID care este tinut intr-un storage care este rapid pe operatii de tip read(e.g. `Redis`).

Cand se trimite un request catre server, browser-ul ataseaza si cookie ul primit de la server in urma autentificarii.  
In cazul in care Cookie Policy-ul este `None`, atunci server-ul va accepta cookies venite de la orice browser.

Spre exemplu, daca user-ul este logat in contul sau de la banca(iar aceasta se afla in cazul din paragraful de mai sus) si apoi intra pe site ul atacatorului, de aici se poate face un request catre server ul bancii prin intermediul caruia sa se transfere suma `X` in contul atacatorului.

**Cateva dintre solutii**:

* folosirea unui CSRF token. Acesta este corelat cu ID ul sesiunii si este stocat pe front end. La fiecare request, se ataseaza acest CSRF token pentru a valida ca, intr adevar, request ul care are cookie ul atasat vine de la sursa sigura
* folosirea unui Cookie Policy mai strict: `Lax`(se pot face) sau `Same-Site`(cel mai strict)

---

## Exemplul 4 - Server-ul accepta non-secure cookies

Non-secure cookies se refera la faptul ca acele cookies nu sunt transmise prin HTTPS. Daca nu are loc criptarea dintre client si server, atacatorul poate observa ce se transmite(care este plain text) si poate obtine informatii valoroase, cum ar fi ID-ul sesiunii unui user.

**Solutia** este folosirea unui mediu sigur de comunicare, cum ar fi HTTPS.

---

## Exemplul 5 - Pornirea server-lui pe 0.0.0.0

Desi, de multe ori, aceasta greseala apare din neatentie, este ceva ce poate fi destul de grav.

`0.0.0.0` inseamna *toate adresele*, cu alte cuvinte, server-ul poate fi accesat la orice adresa. Chiar si intr un network intern, sa spunem al unei companii, poate oferi accesul **oricarui angajat** la un server destinat, sa zicem, **doar adminului**.

Spre exemplu, in Node.js, pornirea unui server in modul urmator:

```javascript
const server http.createServer();

// 0.0.0.0 !!!!
server.listen();
```

*[Sursa.](https://youtu.be/GRGYXJn08W8?t=331)*

va duce la deschiderea server ului pe `0.0.0.0`.

**Solutia** ar fi ce dezvoltatorii sa fie cat mai stricti cu astfel de lucruri

---

## Exemplul 6 - Nevalidarea datelor ce ajung in baza de date

Atacul din acest context poate fi SQL-injection.

De exemplu, intr o aplicatie care foloseste Node + Postgres, se poate folosi direct biblioteca [`pg`](https://node-postgres.com/) care este, totodata, si drive ul pentru postgres.

Daca valorile ce trebuie sa ajunga in query uri sunt inserate direct, atunci exista riscul de SQL-injection.

**Solutia** ar fi sa se foloseasca [*parameterized queries*](https://node-postgres.com/features/queries#parameterized-query). Practic, i se dau bibliotecii valorile pe care vrem sa le includem in query si se va ocupa ea de *sanitizarea* datelor.