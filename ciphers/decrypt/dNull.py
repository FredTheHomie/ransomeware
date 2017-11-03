def decryptNull(key, message):
    # The value inside messageIndex will refer to the index we are
    # currently looking at in message.
    messageIndex = 0
    keyIndex = 0

    plaintext = '' # will contain the decrypted string

    while True:
        # The expression int(key[keyIndex]) will give us the int value of
        # how many nulls to skip over. We will increment the value in
        # messageIndex by this amount.
        messageIndex += int(key[keyIndex])

        if messageIndex >= len(message):
            # When messageIndex is past the last index, we are done.
            break

        # Increment keyIndex so that on the next iteration, we
        # use a number of nulls specified by the next character in key.
        keyIndex += 1
        if keyIndex == len(key):
            keyIndex = 0

        # Append the symbol at messageIndex to the plaintext variable.
        plaintext += message[messageIndex]
        messageIndex += 1

    return plaintext