def caesar_cipher(message, shift, encrypt):
    # encrypt the text provided in message
    if encrypt == 1:
        encrypt = ""
        # print ("encrypt")
        # iterates through each character in the message
        for i in range(0, len(message)):
            # takes the character at index i in the message,
            # converts it to its ASCII representation, adds shift
            # to this ASCII value,ensures its value is between 32 and 126,
            # turns the ASCII value back into a character
            # and adds it to the ciphertext
            character = (ord(message[i]) + shift)
            character = character % 127
            if character < 32:
                character = character + 32
            character = chr(character)
            encrypt += character
        return encrypt

    # decrypt the text provided in message
    elif encrypt == 0:
        plaintext = ""
        # print ("decrypt")
        # iterates through each character in the message
        for i in range(0, len(message)):
            # takes the character at index i in the message,
            # converts it to its ASCII representation, subtracts shift
            # to this ASCII value,ensures its value is between 32 and 126,
            # turns the ASCII value back into a character
            # and adds it to the plaintext
            character = (ord(message[i]) - shift)
            character = character % 127
            if character < 32:
                character = character + 32
            character = chr(character)
            plaintext += character
        return plaintext
    else:
        print("invalid input")


def vigenere_cipher(message, keyword, encrypt):
    encryption = ""
    index = 0  # index which allows for the key to be looped in case the message is longer than it
    for i in range(0, len(message)):
        # calculates the appropriate shift
        shift = ord(keyword[index]) - 32
        # passes the part of the message, shift, and boolean to the caesar cipher
        encryption += caesar_cipher(message[i], shift, encrypt)
        # updates the index accordingly
        index = (index + 1) % len(keyword)

    return encryption


if __name__ == '__main__':
    # each call to the vigenere_cipher function takes in the input message,
    # a keyword representing and an integer representing a boolean value
    ciphertext = vigenere_cipher("hello", "hi", 1)
    print(ciphertext)
    ciphertext1 = vigenere_cipher("1/568", "hi", 0)
    print(ciphertext1)
