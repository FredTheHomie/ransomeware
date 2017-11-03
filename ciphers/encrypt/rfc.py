def RFCencrypt(file):
        rail = [''] * 2
        layer = 0
        for char in file: # For-loop for each character from the string
            rail[layer] += char # Creates the "Fence", in which the "diagonal" characters are placed.
            if layer >= 2 -1:
                layer = 0
            else:
                layer += 1

        cipher =''.join(rail) # Final string once passed through the cipher.
        return cipher