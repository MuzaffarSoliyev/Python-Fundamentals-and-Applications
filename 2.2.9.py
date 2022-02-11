from simplecrypt import decrypt, DecryptionException
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read().strip()

with open('passwords.txt', 'r') as f:
  passwords = f.read().split()
for password in passwords:
  try:
    print(password, decrypt(password, encrypted))
  except DecryptionException:
    print('bad')