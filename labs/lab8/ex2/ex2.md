```bash
gcc -D_PHOTON80_ -D_TABLE_ photon.c photondriver.c -o photon80 sha2.c timer.c -O3
```

```bash
./photon80 -s
# 134 cycles per byte
```

```bash
./photon80 -f
# S = 4, D = 5, Rate = 20, Ratep = 16, DigestSize = 80
```

```bash
python collision-detector.py
# No collisions were found.
```