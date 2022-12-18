> Folosind OpenSSL [3], generați pentru Alice o cheie RSA pe 2048 biți, stocată într-
un fișier alice_sk.pem.

```bash
genrsa -out alice_sk.pem 2048
```

```
Generating RSA private key, 2048 bit long modulus (2 primes)
..........+++++
..............................................................+++++
e is 65537 (0x010001)
```

> Care este valoarea exponentului de criptare?

Valoarea este `65537`.

> Decodați această cheie. Aflați valoarea modulului N și a celor două numere prime
p și q.

```bash
openssl rsa -in alice_sk.pem -text
```

```
RSA Private-Key: (2048 bit, 2 primes)
modulus:
    00:c9:68:c5:02:55:54:a4:f4:63:2e:06:df:8d:0e:
    53:5b:5e:2b:02:6b:27:57:04:b6:0e:a6:7e:79:8e:
    7a:b9:0e:fb:fd:7c:bf:8e:fe:28:c3:0a:c6:ac:5c:
    47:9c:b5:c3:f6:f6:cc:2a:f6:9f:76:16:ea:3f:61:
    d7:fb:12:dc:15:83:06:be:21:2d:c8:ab:51:68:91:
    0c:c4:b4:84:fc:7b:80:be:a7:3b:eb:80:d9:cb:17:
    a9:c5:97:2d:77:d5:0d:ee:fc:b2:0b:cc:fe:83:82:
    b6:e2:c5:4c:80:e0:f6:2e:e4:7b:2f:ed:53:fb:79:
    e1:36:7e:d1:c0:a4:ad:94:65:f6:dd:85:cd:1d:19:
    eb:d6:1a:aa:a1:d4:c2:a6:27:fe:ac:ae:7c:11:cf:
    5d:6f:c2:86:75:9a:c2:9e:c3:6a:50:a6:45:d9:65:
    79:15:7d:5c:4d:97:8d:a8:6e:02:e1:5c:35:44:e6:
    0e:ac:19:24:2e:a3:0b:48:02:5d:93:7f:df:b0:5c:
    03:52:dc:d1:5f:9e:a9:9f:c7:b7:60:ed:fb:79:b7:
    39:16:fd:79:b2:b1:ed:b1:57:6c:ba:ee:9a:66:da:
    57:33:a7:48:28:82:fc:0f:f9:a3:fa:10:6d:17:c0:
    be:49:e1:c9:09:97:c4:69:c9:74:04:df:41:06:d6:
    e9:15
publicExponent: 65537 (0x10001)
privateExponent:
    28:a4:ac:c4:d8:c5:58:f8:3c:1f:68:a1:aa:0c:4f:
    03:ec:0f:cf:d0:21:c3:2c:9f:34:7b:a2:a0:13:01:
    6e:e0:b8:37:21:fa:61:f7:a5:f0:1d:f7:93:86:97:
    a8:e7:01:21:90:12:09:45:75:4e:56:37:75:0c:e0:
    91:b8:ef:92:a3:bb:33:98:ec:6d:47:2d:09:65:e3:
    e6:b9:ea:f0:2c:58:01:a1:2b:b5:4d:6e:25:ce:a3:
    a2:cc:ec:0e:f7:7e:75:50:a6:f9:3c:a7:cb:90:10:
    29:d8:d8:a4:55:41:38:9b:40:c4:9e:26:c9:63:81:
    f0:06:4d:7b:8b:7f:bf:a7:2c:1d:69:1c:f2:c3:4a:
    b5:f8:96:c0:f7:1f:52:6c:df:a7:fa:5b:63:2c:6a:
    f1:4f:e2:19:5a:e4:92:c9:40:b8:96:35:77:23:b7:
    c8:67:aa:02:3c:a2:d6:10:65:15:67:df:03:00:d5:
    8d:30:10:a2:f0:99:4a:80:58:41:ca:5e:98:91:88:
    c9:09:9e:92:c0:9e:2e:e2:fb:06:41:50:ac:42:dd:
    d2:29:55:f6:e7:8c:2a:68:ac:bb:7f:6b:b1:3c:41:
    c5:8d:e6:8e:5c:2d:a9:51:2f:3d:69:c2:af:95:6d:
    85:ad:d9:1f:9f:a3:1d:aa:43:84:a2:33:54:36:8f:
    c1
prime1:
    00:ec:c8:24:b7:8d:cb:91:9f:62:2a:d7:a2:e0:93:
    ea:9d:65:19:0b:c0:6f:c0:23:f9:ec:d2:8a:d7:37:
    bb:73:91:19:0a:7c:a8:bd:ff:48:2a:c6:2b:23:2a:
    b3:d7:73:78:a7:07:6c:f8:48:6c:57:77:e9:5d:f4:
    bf:6d:a6:c6:68:12:a3:ab:82:af:ee:9c:29:ec:cd:
    f3:87:cc:db:2a:df:f0:bc:ca:d5:e3:bb:75:ea:ed:
    99:05:e7:95:b0:35:44:fb:d0:a0:32:ca:64:a0:a5:
    43:7f:92:1d:98:a8:02:3b:19:27:31:44:b5:92:fb:
    6a:a8:b2:de:68:68:81:67:65
prime2:
    00:d9:c1:a7:93:93:fc:62:6f:7d:63:2b:46:25:04:
    79:13:86:39:40:97:87:2d:af:ec:12:f6:b9:78:a8:
    a2:e3:c3:09:90:0b:29:80:38:09:20:d8:4e:19:df:
    b5:94:40:b5:ba:97:0f:bc:02:82:46:6e:a7:52:66:
    f4:72:b8:1e:5e:87:bf:3f:29:09:69:53:fe:3b:cb:
    2a:b1:fb:dc:53:54:1e:0e:67:da:13:aa:d2:42:b8:
    cf:5b:1c:6f:fc:29:f5:27:f0:57:96:97:7f:aa:6c:
    74:e5:bc:27:17:b2:45:e0:38:27:a7:d3:94:93:50:
    a6:46:f0:19:82:10:68:97:f1
```

> Cheia lui Alice nu este protejată în niciun fel, deci este vulnerabilă. Alegeți o
parolă puternică și generați o nouă cheie protejată folosind această parolă și
AES256.

```bash
openssl genrsa -aes256 -out alice_sk.pem
```

```
Generating RSA private key, 2048 bit long modulus (2 primes)
..................................................................+++++
.+++++
e is 65537 (0x010001)
Enter pass phrase for alice_sk.pem:
Verifying - Enter pass phrase for alice_sk.pem:
```

> Ce diferențe observați? Decodați această cheie folosind parola folosită la creare.

Se specifica faptul ca este criptata cheia privata, dar si ce algoritm a fost folosit pentru asta:

```
cat alice_sk.pem 
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-256-CBC,0C1C36EBD264830E87AE01968B89FDA6

...
```

Decriptarea:

```bash
openssl rsa -in alice_sk.pem
```

Rezultat:

```
Enter pass phrase for alice_sk.pem:
writing RSA key
-----BEGIN RSA PRIVATE KEY-----
```

> Care este valoarea exponentului de criptare? Ce observați? Impactează această
alegere securitatea?

Valoarea exponentului este la fel, `65537`.

> Exportați cheia publică a lui Alice în fișierul alice_pk.pem. Decodați această cheie
pentru a vedea valorile modulului și exponentului.

```bash
openssl rsa -in alice_sk.pem -RSAPublicKey_out -out alice_pk.pem
Enter pass phrase for alice_sk.pem:
writing RSA key
```

```bash
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAqCHAe/L9VR1dyKejkwq8nt/MpOIRc1WMk4YEmYI6Hzk4cBkRNew0
RwNGBshckjbivHqXr9h93RoQPb18yVpZUVDGp0n7oYrZrUMEjcsDlnM7hP+yxwED
Z/B0/ivenqJTIOcUEe7tbdM8mAwZChLS57byJXc0tnP07M+WOO+utZMBcXOFk3Ze
dtV5+OaHveNpINzDoXDkmo8JySje7ofWfiWdSCJ8pN+elOA5+xUb4unv/51QvpA8
M9ad0FGR/FJE2XM3A3SHqleuQ1tOZSwCWFGld8pIR4YzXk0kgJLnGefYIAAXfnty
x53j3ckRcij3Vq6Kb9VTxhsS01aGGEBPCQIDAQAB
-----END RSA PUBLIC KEY-----
```

Decorarea:

```bash
openssl rsa -in alice_pk.pem -text -RSAPublicKey_in
```

Rezultat:

```
RSA Public-Key: (2048 bit)
Modulus:
    00:a8:21:c0:7b:f2:fd:55:1d:5d:c8:a7:a3:93:0a:
    bc:9e:df:cc:a4:e2:11:73:55:8c:93:86:04:99:82:
    3a:1f:39:38:70:19:11:35:ec:34:47:03:46:06:c8:
    5c:92:36:e2:bc:7a:97:af:d8:7d:dd:1a:10:3d:bd:
    7c:c9:5a:59:51:50:c6:a7:49:fb:a1:8a:d9:ad:43:
    04:8d:cb:03:96:73:3b:84:ff:b2:c7:01:03:67:f0:
    74:fe:2b:de:9e:a2:53:20:e7:14:11:ee:ed:6d:d3:
    3c:98:0c:19:0a:12:d2:e7:b6:f2:25:77:34:b6:73:
    f4:ec:cf:96:38:ef:ae:b5:93:01:71:73:85:93:76:
    5e:76:d5:79:f8:e6:87:bd:e3:69:20:dc:c3:a1:70:
    e4:9a:8f:09:c9:28:de:ee:87:d6:7e:25:9d:48:22:
    7c:a4:df:9e:94:e0:39:fb:15:1b:e2:e9:ef:ff:9d:
    50:be:90:3c:33:d6:9d:d0:51:91:fc:52:44:d9:73:
    37:03:74:87:aa:57:ae:43:5b:4e:65:2c:02:58:51:
    a5:77:ca:48:47:86:33:5e:4d:24:80:92:e7:19:e7:
    d8:20:00:17:7e:7b:72:c7:9d:e3:dd:c9:11:72:28:
    f7:56:ae:8a:6f:d5:53:c6:1b:12:d3:56:86:18:40:
    4f:09
Exponent: 65537 (0x10001)
writing RSA key
```