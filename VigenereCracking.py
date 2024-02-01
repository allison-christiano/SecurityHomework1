def shift_message(encrypted_message, shift):
    # shifts the letter by a key value designated by shift and returns it to the get_caesar_shift function
    plaintext = ""
    for character in encrypted_message:
        # if the character is alphabetic, apply the shift and find the new probable plaintext value
        # if not, add it to the plaintext
        if character.isalpha():
            character = ord(character)
            character = (character - shift - 65) % 26 + 65
            character = chr(character)
        plaintext += character
    return plaintext

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


def cross_correlation(dict1, dict2):
    # iterates through the 2 dictionaries and calculates the cross correlation using the formula
    # provided in the notes
    cross_correlation_val = 0
    for key in dict1.keys():
        cross_correlation_val += dict1[key] * dict2[key]
    return cross_correlation_val


def get_caesar_shift(enc_message, expected_dist):
    # sets the probable shift and correlation to -1 and will be overwritten
    # if the function behaves as desired
    probable_shift = -1
    probable_correlation = -1
    # iterates through all possible key values, shifts the encrypted
    # message by i, runs a frequency analysis of this shifted message
    # computes a cross correlation between this frequency analysis and English
    # finds the highest correlation, and suggests the shift value accordingly
    for i in range(0, 26):
        possible_plaintext = shift_message(enc_message, i)
        possible_plaintext_freq = frequency_analysis(possible_plaintext)
        correlation = cross_correlation(possible_plaintext_freq, expected_dist)
        if correlation > probable_correlation:
            probable_correlation = correlation
            probable_shift = i
    return probable_shift


if __name__ == '__main__':
    message = "CQN ARPQCB XO NENAH VJW JAN MRVRWRBQNM FQNW CQN ARPQCB XO XWN VJW JAN CQANJCNWNM"
    freq_dist = {' ': .1828846265, 'E': .1026665037, 'T': .0751699827, 'A': .0653216702, 'O': .0615957725,
                 'N': .0571201113, 'I': .0566844326, 'S': .0531700534, 'R': .0498790855, 'H': .0497856396,
                 'L': .0331754796, 'D': .0328292310, 'U': .0227579536, 'C': .0223367596, 'M': .0202656783,
                 'F': .0198306716, 'W': .0170389377, 'G': .0162490441, 'P': .0150432428, 'Y': .0142766662,
                 'B': .0125888074, 'V': 0.0079611644, 'K': 0.0056096272, 'X': 0.0014092016, 'J': 0.0009752181,
                 'Q': 0.0008367550, 'Z': 0.0005128469}

    probable_shift_value = get_caesar_shift(message, freq_dist)
    print(probable_shift_value)
