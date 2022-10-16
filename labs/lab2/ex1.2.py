
import base64

# `C = M + K`
# Here, we're given `M` and `C` and we must find `K`.
# `C + M = M + K + M = K`

ENCODED_MESSAGE = 'o9/khC3Pf3/9CyNCbdzHPy5oorccEawZSFt3mgCicRnihDSM8Obhlp3vviAVuBbiOtCSz6husBWqhfF0Q/8EZ+6iI9KygD3hAfFgnzyv9w=='
DECRYPTED_MESSAGE = 'Orice text clar poate obtinut dintr-un text criptat cu OTP dar cu alta cheie..'

encryptedMessageBytes = base64.b64decode(ENCODED_MESSAGE)
decryptedMessageBytes = bytearray.fromhex(str.encode(DECRYPTED_MESSAGE).hex())

# print(encryptedMessageBytes)
# print(len(encryptedMessageBytes))
# print(decryptedMessageBytes)
# print(len(decryptedMessageBytes))

for encryptedMsgByte, decryptedMsgByte in zip(encryptedMessageBytes, decryptedMessageBytes):
  # binaryResult = bin(encryptedMsgByte ^ decryptedMsgByte)
  # print(binaryResult[2:], end='')

  hexResult = hex(encryptedMsgByte ^ decryptedMsgByte)
  print(hexResult[2:], end='')
