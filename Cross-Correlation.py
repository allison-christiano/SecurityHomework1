def cross_correlation(dict1, dict2):
    # iterates through the 2 dictionaries and calculates the cross correlation using the formula
    # provided in the notes
    cross_correlation_val = 0
    for key in dict1.keys():
        cross_correlation_val += dict1[key] * dict2[key]
    return cross_correlation_val


if __name__ == '__main__':
    symbols = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ '''
    # makes the symbols dictionary
    freq1_dict = {}
    freq2_dict = {}
    freq3_dict = {}
    # creates key values for every item in symbols for each set
    for character in symbols:
        freq1_dict[character] = 0
        freq2_dict[character] = 0
        freq3_dict[character] = 0

    # modifies the values as set on the assignment for each set
    freq1_dict['A'] = 0.012
    freq1_dict['B'] = 0.003
    freq1_dict['C'] = 0.01
    freq1_dict['D'] = 0.1
    freq1_dict['E'] = 0.02
    freq1_dict['F'] = 0.001

    freq2_dict['A'] = 0.001
    freq2_dict['B'] = 0.012
    freq2_dict['C'] = 0.003
    freq2_dict['D'] = 0.01
    freq2_dict['E'] = 0.1
    freq2_dict['F'] = 0.02

    freq3_dict['A'] = 0.1
    freq3_dict['B'] = 0.02
    freq3_dict['C'] = 0.001
    freq3_dict['D'] = 0.012
    freq3_dict['E'] = 0.003
    freq3_dict['F'] = 0.01

    # calculates the cross correlation for sets 1 & 2 and prints the result to the screem
    cross12_dict = cross_correlation(freq1_dict, freq2_dict)
    print(cross12_dict)

    # calculates the cross correlation for sets 1 & 3 and prints the result to the screen
    cross13_dict = cross_correlation(freq1_dict, freq3_dict)
    print(cross13_dict)
