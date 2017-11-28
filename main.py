from ciphers.encrypt.allEncrypt import fileEncrypt
from ciphers.decrypt.allDecrypt import fileDecrypt
from util.utils import (getRandomKey,
                        getUID)

key = getRandomKey()
##fileEncrypt(key)
fileDecrypt(key)