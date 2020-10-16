character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# function modular multiplicative inverse
def modInverse(key, numchar) :
  for x in range(1, numchar) :
    if ((key * x) % numchar == 1) :
      return x
  return 1

def Multiplicative_decrypt(plaintext, key):
  outText = []
  decryptText = []
  for eachLetter in plaintext:
    if eachLetter in character:
      # index letters
      index = character.index(eachLetter)
      # C = (P * K^-1) mod 26
      decrypt = (index * modInverse(key, 26)) % 26
      decryptText.append(decrypt)
      newLetter = character[decrypt]
      outText.append(newLetter)
  return outText

text = input ('Type text to Decrypt: ')
plaintext = str(text)
num = input('Type key between 0-25: ')
key = int(num)
print('Decrypt Text:' ,*Multiplicative_decrypt(plaintext, key))
