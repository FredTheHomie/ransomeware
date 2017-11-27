# Importing function from the utilities file
from util.utils import offset

def DecryptRailsFenceCipher(key, encrypted):
    showOff = 0
    array = [[' ' for col in range(len(encrypted))] for row in range(key)] # Gets the columns and rows of the "Fence"
    read = 0

    for rail in range(2): # Will get the order of the words in which they appear on in the fence, and order them back to their orginal locations
        pos = offset(1, 2, rail)
        even = 0

        if rail == 0:
            pos = 0
        else:
            pos = int(pos / 2)

        while pos < len(encrypted):
            if read == len(encrypted):
                break

            array[rail][pos] = encrypted[read]
            read += 1

            pos += offset(even, 2, rail)
            even = not even

    if showOff:
        for row in array:
            print row

    decoded = ''

    for x in range(len(encrypted)):
        for y in range(2):
            if array[y][x] != ' ':
                decoded += array[y][x]

    return decoded