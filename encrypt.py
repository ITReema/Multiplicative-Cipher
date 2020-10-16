character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Multiplicative_encrypt(Plaintext, key):
    outText = []
    cryptText = []
    for eachLetter in Plaintext:
        if eachLetter in character:
            # index letters 
            index = character.index(eachLetter)
            # C = (P * K) mod 26
            crypting = (index * key) % 26
            cryptText.append(crypting)
            newLetter = character[crypting]
            outText.append(newLetter)
    return outText

text = input ('Type text to encrypt: ')
plaintext = str(text)
num = input('Type key between 0-25: ')
key = int(num)
print('Ciphertext:' ,*Multiplicative_encrypt(plaintext, key)) 