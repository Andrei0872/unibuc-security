> Ce impact are refolosirea cheii de la pct.1 pentru o altă criptare?

Refolosirea cheii poate duce la *scurgeri de informatii*(information leakage):

```python
# Primul mesaj criptat.
E1 = M1 + K

# Al doilea mesaj criptat.
E2 = M2 + K
```

Daca ar fi sa aplicam XOR pe `E1` si `E2`:

```python
E1 + E2 = M1 + K + M2 + K = M1 + M2
```

In rezultatul de mai sus apare scurgerea de informatii. Spre exemplu, la laborator sa prezentat exemplul in care `M1` este o imagine ce are doar un cap, iar `M2` care are doar trupul. Din `M1 + M2` poate iesi imaginea *intreaga*.

## Surse

* [Exemplu de *information leakage* folosind imagini](https://crypto.stackexchange.com/a/108)