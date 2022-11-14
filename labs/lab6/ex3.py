from Crypto.Cipher import DES

"""
E(K2, E(K1, M)) = C; apply D(K2)
E(K1, M) = D(K2, C).

So, we build a look-up table following this pattern: `{ [E(Ki, M)]: Ki }`. (`Ki` = each possible key).
Then, for each Ki, we decrypt the ciphertext and see whether the result can be found in the lookup table.
If yes, then we've found the pair.

_Check Lab6 for more details_.
\\x?0, so, in order to find `?`, we need to loop through 0...240 by incrementing by 16. 240 because the last possible value of `?` can be `F` and `\\xF0 = 240`.
"""

PLAINTEXT = "Provocare MitM!!"
CIPHERTEXT = b"G\xfd\xdfpd\xa5\xc9'C\xe2\xf0\x84)\xef\xeb\xf9"

def generatePossibleKey (potentialHexSymbol):
  return bytearray([potentialHexSymbol, 0, 0, 0, 0, 0, 0, 0])

# Create table.
def createLookupTable ():
  global PLAINTEXT

  table = {}
  for potentialHexSymbol in range(0, 241, 16):
    key = generatePossibleKey(potentialHexSymbol)
    cipher = DES.new(key, DES.MODE_ECB)

    ciphertext = cipher.encrypt(PLAINTEXT.encode())
    table[ciphertext] = key
  
  return table

# Find key based on the table(i.e. using the MitM attack).
def findKeysPair (lookupTable):
  global CIPHERTEXT

  for potentialHexSymbol in range(0, 241, 16):
    key = generatePossibleKey(potentialHexSymbol)
    cipher = DES.new(key, DES.MODE_ECB)

    decrypted_text = cipher.decrypt(CIPHERTEXT)

    if decrypted_text in lookupTable:
      matching_key = lookupTable[decrypted_text]
      return (matching_key, key)

table = createLookupTable()
keys_pair = findKeysPair(table)
# print(keys_pair)

key1, key2 = keys_pair

# key1 = b'\x80\x00\x00\x00\x00\x00\x00\x00'
# key2 = b'\xe0\x00\x00\x00\x00\x00\x00\x00'

cipher1 = DES.new(key1, DES.MODE_ECB)
cipher2 = DES.new(key2, DES.MODE_ECB)

plaintext = b'Provocare MitM!!'
ciphertext = cipher2.encrypt(cipher1.encrypt(plaintext))
print(ciphertext)