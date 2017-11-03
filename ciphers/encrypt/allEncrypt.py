# Importing all functions and variables from other modules
from affine import encryptMessage
from rfc import RFCencrypt
from null import encryptNull
from util.utils import (warning,
                        file)

# This function intakes the string and passes it through all 3 ciphers.
def superEncrypt(obj):
    final = ''
    rails = RFCencrypt(obj) # Rails Fence Cipher
    affine = encryptMessage(rails) # Affine Cipher
    null = encryptNull('302', affine) # Null Cipher
    final = null # This is the final string, once passed through all 3 ciphers
    return final

# This function encrypts the file using the superEncrypt() function
def fileEncrypt():
    f = open(file, 'r+')
    g = f.read()
    s = superEncrypt(g)
    f.seek(0)
    f.truncate()
    f.write(warning + s)
    f.close()