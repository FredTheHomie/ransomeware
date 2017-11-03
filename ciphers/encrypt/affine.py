# Importing variables and functions from utilities file
from util.utils import (SYMBOLS,
                        getKeyParts)

def encryptMessage(message):
    key = 97
    keyA, keyB = getKeyParts(key) # Splits the keys into 2 different keys
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # Encrypts the symbol
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol  # Appends this symbol unencrypted
    return ciphertext