import secrets
import string
import hashlib

"""
- password: min 10 chars
- at least 1 uppercase letter
- at least 1 lowercase letter
- at least 1 digit
- at least 1 special char: '.!$@'

Usage: generating a temporary password. It may be used, for example, by banks when they generate
a temporary password so that the user can change it as soon as possible with their new, secure password.
"""
SPECIAL_CHARS = ".!$@"
def generate_password ():
  fns = [
    lambda : secrets.choice(string.ascii_lowercase),
    lambda : secrets.choice(string.ascii_uppercase),
    lambda : secrets.choice(string.digits),
    lambda : secrets.choice(SPECIAL_CHARS),
  ]

  while True:
    password = ''.join([secrets.choice(fns)() for i in range(10)])

    if is_password_valid(password):
      break

  return password

def is_password_valid (password: str):
    return True if (
      any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and any((sc in password) for sc in SPECIAL_CHARS)
    ) else False

"""
URL-safe = can be put in the URL bar.

Usage: generating a short-lived URL that will allow a user to reset their password.
The generated URL-safe string would be part of the link that would be sent to the user via email.
"""
def generate_url_safe ():
  return secrets.token_urlsafe(32)

"""
Usage: *tokenization*, i.e. substituting sensitive data(e.g. PII) with a randomly generated token. There is no
mathematical connection between the generated string and the sensitive data, so, if an attacker
gets hold of the token, there isn't much they can do.
The use case is detailed here: https://www.skyflow.com/post/demystifying-tokenization-what-every-engineer-should-know, in the *What Problems Does Tokenization Solve?* section. 
"""
def generate_hex_token ():
  return secrets.token_hex(32)

"""
It reduces the risk of timing attacks because it compares the string
in constant time.
"""
def compare_sequences (seq1, seq2):
  return secrets.compare_digest(seq1, seq2)

"""
https://justcryptography.com/how-to-create-secure-keys-for-symmetric-encryption/
"""
def generate_encryption_key ():
  # 8 chars must be encrypted. 1 char = 8 bits -> 800 bits in total.
  return secrets.randbits(800)

"""
The passwords must be securely stored. Encryption is not a good candidate for that
as they are paired with a **secret key**.
What we can do instead is to **hash** the password. Hashing a password will produce
an irreproducible result, meaning the hash digest(i.e. the output of the hash function)
can't be reversed in order to the initial data.
It's important to mention that a hash function would yield the same values for the same inputs.
In order to mitigate that, we can use a **salt**, which is a cryptographically-secure generated
value that is added to the raw password. The resulting string would then be hashed.
"""
def store_password (raw_pass: str):
  salt = generate_hex_token()
  hashed_pass = hashlib.sha256((raw_pass + salt).encode())

  return hashed_pass.hexdigest()

# print(generate_password())
# print(generate_url_safe())
# print(generate_hex_token())
# print(compare_sequences("andrei", "andrei"))
# print(generate_encryption_key())

# Different values! - due to using a `salt`.
print(store_password("andrei"))
print(store_password("andrei"))