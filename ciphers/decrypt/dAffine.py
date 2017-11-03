# Import the functions and variables from the utilities file
from util.utils import (SYMBOLS,
                        getKeyParts,
                        cryptomath,
                        checkKeys)

def decryptMessage(message):
     key = 97
     keyA, keyB = getKeyParts(key) # Takes the key value and splits it into 2 keys
     checkKeys(keyA, keyB, 'decrypt') # Checks that the key values are correct
     plaintext = ''
     modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

     # For-loop for each character in the message
     for symbol in message:
         if symbol in SYMBOLS:
             symIndex = SYMBOLS.find(symbol)
             plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
         else:
             plaintext += symbol # Final string once passed through the cipher
     return plaintext
