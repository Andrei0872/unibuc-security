from Crypto.Cipher import AES
from Crypto.Util import Padding

key = b'O cheie oarecare'
data = b'testtesttesttesttesttesttesttesttesttesttesttest'

cipher = AES.new(key, AES.MODE_ECB)
result = cipher.encrypt(data)

# print(result)
# print(cipher.decrypt(result))

# print(len(data))
# print(len('testtesttesttesttesttesttesttesttesttesttesttest'))
# print(len(key))

data = b'test'
data = Padding.pad(data, 16)

cipher = AES.new(key, AES.MODE_ECB)
result = cipher.encrypt(data)

# print(result)
# print(cipher.decrypt(result))


header = b'header or associated data - not encrypted!'
data = b'nobody needs to know this!!'
key = Padding.pad(b'nobody would guess this', 16)

cipher = AES.new(key, AES.MODE_EAX)
cipher.update(header)

ciphertext, tag = cipher.encrypt_and_digest(data)

print(ciphertext)