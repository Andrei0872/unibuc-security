
> Ce problemă identificați în următoarele secvențe de cod?

An ambele cazuri, problema este aceea ca se foloseste **acelasi seed** pentru inceput. Concret, daca se apeleaza `generateAccoundID` de 2 ori, rezultatul o sa fie acelasi. Pe alta parte, daca `generateSessionID` este apelata cu acelasi user ID(i.e. pentru acelasi user), ID ul sesiunii o sa fie acelasi.

> Care este CWE ID asociat scenariilor de mai sus si problemei pe care acestea o
ridică?

ID ul este [336](https://cwe.mitre.org/data/definitions/336.html).

> Ce se întâmplă dacă nu se folosește același seed de fiecare dată, dar spațiul seed-urilor
posibile este mic? Puteți găsi un CWE ID corespunzător acestui caz?

Daca spatiul seed-urilor este mic(e.g. obtinem doar 2 bytes random de la sistemul de operare), atunci atacatorul poate sa faca **brute force** pentru a determina ce alte posibilitati de victime ar exista.

CWE ID-ul corespunzator este [339](https://cwe.mitre.org/data/definitions/339.html).

> Căutați atacul identificat la punctul precedent în [5]. Identificați și aici o mențiune la seed?

Este vorba de atacul *Small Seed Space in PRNG*. In exemplul dat, seed-ul rezulta din obtinerea a 2 bytes random de la sistemul de opereare. Problema este ca spatiul de posibilitati este mic, desi ele sunt complet random(din moment ce sunt venite de la sistemul de operare).

> Găsiți alte utilizări defectuoase ale PRG explicate în alte CWE-uri. Există CVE-uri
corespunzătoare acestora?

Un alt CWE este [CWE-335](https://cwe.mitre.org/data/definitions/335.html), care se leaga de utilizarea incorecta a seed-urilor in PRGs. Un PRG este determinist, asta insemnand ca numerele generate, desi par random, in esenta ele sunt generate folosind un anumte *pattern*. Prin urmare, este esential ca seed-urile(i.e. punctul de plecare pentru un PRG) sa fie cat mai *sigure* din punct de vedere criptografic.  
Un CVE rezultat din acest *weakness* este [CVE-2020-7010](https://www.cve.org/CVERecord?id=CVE-2020-7010), unde serviciul de cloud ECK genera parole folosind un seed slab. Daca punctul de plecare este unul *nesigur*, atunci atacatorul poate ghici seed-ul initial si, prin urmare, si restul de numere generate de PRG.

Un alt CWE este [CWE-337: Predictable Seed in Pseudo-Random Number Generator (PRNG)](https://cwe.mitre.org/data/definitions/337.html). Un exemplu de seed predictibil este data curenta. Un CVE legat de acest CWE este [CVE-2008-0166](https://www.cve.org/CVERecord?id=CVE-2008-0166), unde, pentru generarea seed-ului, se folosea ID-ul procesului curent.

> Căutați înregistrări CVE care se referă la vulnerabilități în legătură cu PRG. Câte ați
identificat ca fiind definite în acest an?

Am descoperit [CVE-2022-39218](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39218). Mai multe detalii, inclusiv cum a fost mitigata vulnerabilitate, pot fi gasite [aici](https://github.com/fastly/js-compute-runtime/security/advisories/GHSA-cmr8-5w4c-44v8).