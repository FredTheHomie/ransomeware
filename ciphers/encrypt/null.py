import random

def encryptNull(key, message):
    # The expression int(key[keyIndex]) will be used to decide how many
    # nulls should be inserted. For example, if key is the value '570'
    # and keyIndex is 0, then 5 null characters will be inserted into
    # the ciphertext.
    keyIndex = 0

    ciphertext = '' # will contain the encrypted string
    for symbol in list(message) + [None]:
        for dummy in range(int(key[keyIndex])):
            # Add a null.
            ciphertext += random.choice(message)

        if symbol == None:
            break # the None value marks the end

        # Increment keyIndex so that on the next iteration, we use a
        # number of nulls specified by the next character in key.
        keyIndex += 1
        if keyIndex == len(key):
            # keyIndex is past the end, so reset it back to 0.
            keyIndex = 0

        # Add the real symbol after adding the nulls.
        ciphertext += symbol
    return ciphertext