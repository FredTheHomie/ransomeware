# Importing all functions and variables from other modules
from dAffine import decryptMessage
from drfc import DecryptRailsFenceCipher
from dNull import decryptNull
from util.utils import (warning,
                        file)

# This method decrypts the final product cipher. It executes the decryption
# ciphers in the opposite order in which the encryption ciphers
# were executed
def superDecrypt(obj):
    final = ''
    null = decryptNull('302', obj) # Null Cipher Decryption
    rails = DecryptRailsFenceCipher(null) # Rails Fence Cipher Decryption
    affine = decryptMessage(rails) # Affine Cipher Decryption
    final = affine # This is now the original contents of the file
    return final

# This function decrypts the file using the superDecrypt() function
def fileDecrypt():
    f = open(file, 'r+') # This opens the file
    g = f.read() # Reads the file
    n = g.replace(warning, '') # Removes the instructions once the decryption is made.
    s = superDecrypt(n)
    f.seek(0) # Removes the contents of the file
    f.truncate()
    f.write(s)
    f.close()