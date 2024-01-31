def frequency_analysis(string):
    symbols = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ '''
    sym_len = len(symbols)
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


if __name__ == '__main__':
    returnDictionary = frequency_analysis("AAAAAA ")
    print(returnDictionary)
