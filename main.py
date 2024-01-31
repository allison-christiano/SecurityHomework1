def caesar_cipher(message, shift, encrypt):
    # encrypt the text provided in message
    if encrypt == 1:
        ciphertext = ""
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
            ciphertext += character
        return ciphertext

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


if __name__ == '__main__':
    # each call to the caesar_cipher function takes in the input message
    # the number you would like to shift and an integer representing a boolean value
    encryption = caesar_cipher('Hello world', 5, 1)
    decryption = caesar_cipher('Mjqqt%|twqi', 5, 0)
    print(encryption)
    print(decryption)
