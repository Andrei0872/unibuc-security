import base64

# Note: `+` == XOR.
# `C = M + K`, here we're given the `K` and `C` and we need to find out `M`.
# `C + K = M + K + K = M`.

# Base64.
ENCODED_MESSAGE = 'o9/khC3Pf3/9CyNCbdzHPy5oorccEawZSFt3mgCicRnihDSM8Obhlp3vviAVuBbiOtCSz6husBWqhfF0Q/8EZ+6iI9KygD3hAfFgnzyv9w=='

KEY = 'ecb181a479a6121add5b42264db9b44b4b48d7d93c62c56a3c3e1aba64c7517a90ed44f8919484b6ed8acc4670db62c249b9f5bada4ed474c9e4d111308b614788cd4fbdc1e949c1629e12fa5fdbd9'

decodedMessageBytes = base64.b64decode(ENCODED_MESSAGE)
keyBytes = bytearray.fromhex(KEY)

for msgByte, keyByte in zip(decodedMessageBytes, keyBytes):
  print(chr(msgByte ^ keyByte), end='')