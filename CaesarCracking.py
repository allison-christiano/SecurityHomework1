def cross_correlation(dict1, dict2):
    # iterates through the 2 dictionaries and calculates the cross correlation using the formula
    # provided in the notes
    cross_correlation_val = 0
    for key in dict1.keys():
        cross_correlation_val += dict1[key] * dict2[key]
    return cross_correlation_val


def frequency_analysis(string):
    symbols = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ '''
    # makes the symbols dictionary
    symbols_dict = {}
    # creates key values for every item in symbols
    for character in symbols:
        symbols_dict[character] = 0
    # makes each dictionary entry a count of how many of that letter appear in the string
    for letter in string:
        symbols_dict[letter] = (symbols_dict[letter] + 1)
    # calculates the frequency of each count value
    for entry in symbols_dict:
        symbols_dict[entry] = symbols_dict[entry] / len(string)
    return symbols_dict


def shifted(message1, shift_val):
    plaintext = ""
    for char in message:
        if char.isalpha():
            # iterates through each character in the message
            for i in range(0, len(message1)):
                # takes the character at index i in the message,
                # converts it to its ASCII representation, subtracts shift
                # to this ASCII value, ensures the character is in upper case
                # turns the ASCII value back into a character
                # and adds it to the plaintext
                character = (ord(message1[i]) - shift_val)
                character = character % 127
                character = chr(character)
                character.upper()
                plaintext += character
            else:
                plaintext += char
    return plaintext


def get_caesar_shift(enc_message, expected_dist):
    probable_key = -1
    enc_freq = frequency_analysis(enc_message)
    # print(enc_freq)
    cross_val1 = cross_correlation(enc_freq, expected_dist)
    # print(cross_val1)
    max_val = -1
    for i in range(0, 26):
        probable_message = shifted(enc_message, i)
        print(i)
        probable_freq = frequency_analysis(probable_message)
        cross_val2 = cross_correlation(probable_freq, expected_dist)
        if cross_val2 > max_val:
            max_val = cross_val2
            probable_key = i

    return probable_key


if __name__ == '__main__':
    freq_dist = {' ': .1828846265, 'E': .1026665037, 'T': .0751699827, 'A': .0653216702, 'O': .0615957725,
                 'N': .0571201113, 'I': .0566844326, 'S': .0531700534, 'R': .0498790855, 'H': .0497856396,
                 'L': .0331754796, 'D': .0328292310, 'U': .0227579536, 'C': .0223367596, 'M': .0202656783,
                 'F': .0198306716, 'W': .0170389377, 'G': .0162490441, 'P': .0150432428, 'Y': .0142766662,
                 'B': .0125888074, 'V': 0.0079611644, 'K': 0.0056096272, 'X': 0.0014092016, 'J': 0.0009752181,
                 'Q': 0.0008367550, 'Z': 0.0005128469}
    message = "CQN ARPQCB XO NENAH VJW JAN MRVRWRBQNM FQNW CQN ARPQCB XO XWN VJW JAN CQANJCNWNM"
    # print(freq_dist)
    # print(message)
    key_val = get_caesar_shift(message, freq_dist)
    print(key_val)
