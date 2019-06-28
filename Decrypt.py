key= 'abcdefghijklmnopqrstuvwxyz'

def decrypt(n, ciphertext):

    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

text = "n fr htinsl udymts!"
offset = 5

decrypted = decrypt(offset, text)
print('Decrypted:', decrypted)
