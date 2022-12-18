
> Jucați rolul lui Bob. Criptați fișierul bob_message.txt folosind RSA [4] și cheia
generată anterior. Încercați să criptați fișierul bob_message.rtf folosind RSA [4] și
cheia generată anterior. Ce observați? De ce se întâmplă aceasta?

```bash
openssl pkeyutl -sign -in bob_message.txt -inkey alice_sk.pem -out bob_message_eng.txt
```

Incercand pe `*.rtf`:

```bash
openssl pkeyutl -sign -in bob_message.rtf -inkey alice_sk.pem -out bob_message_eng.txt
```

Output:

```
Enter pass phrase for alice_sk.pem:
Error: The input data looks too long to be a hash
```

> Folosiți criptarea hibridă pentru a cripta mesajul lui Bob către Alice. Pentru
aceasta, generați o cheie simetrică pe 256 biți (32 bytes) și folosiți această cheie
pentru criptarea fișierului bob_message.rtf cu AES-CTR [5]. Criptați noua cheie
asimetric, folosind RSA.

```bash
openssl rand 32 > bob.key
```

`bob_message.rtf`:

```bash
openssl enc -aes256 -a -in bob_message.rtf -out bob_message_enc.rtf -kfile bob.key
```

```bash
openssl pkeyutl -sign -in bob.key -inkey alice_sk.pem -out bob_key_enc.key
```

> Jucați rolul lui Alice. Folosiți fișierele criptate primite (criptarea cheii AES
folosind RSA și criptarea mesajului folosind AES-CTR), decriptați și obțineți
mesajul inițial.

```bash
openssl enc -aes256 -d -in bob_message_enc.rtf -kfile bob_key_enc.key
```