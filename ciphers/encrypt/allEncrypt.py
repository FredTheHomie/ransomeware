# Importing all functions and variables from other modules
from affine import encryptMessage
from rfc import RFCencrypt
from null import encryptNull
from util.utils import (warning,
                        file,
                        getRandomKey)

# This function intakes the string and passes it through all 3 ciphers.
def superEncrypt(key, obj):
    final = ''
    rails = RFCencrypt(key, obj) # Rails Fence Cipher
    affine = encryptMessage(key, rails) # Affine Cipher
    nullC = encryptNull(str(key), affine) # Null Cipher
    final = nullC # This is the final string, once passed through all 3 ciphers
    return final

# This function encrypts the file using the superEncrypt() function
def fileEncrypt(key):
    f = open(file, 'r+')
    g = f.read()
    s = superEncrypt(key, g)
    f.seek(0)
    f.truncate()
    f.write(warning + s)
    f.close()