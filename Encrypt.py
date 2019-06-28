key= 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):

    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

text = "I am coding Python!"
offset = 5

encrypted = encrypt(offset, text)
print('Encrypted:', encrypted)