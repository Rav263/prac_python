from collections import Counter
from math import ceil

def xehs(string):
    byte_string = bytes(string, "ASCII") 

    return sum(64**(len(byte_string) - i - 1) * (byte_string[i] - 32) for i in range(len(byte_string)))


def shex(number):
    list_of_bytes = list()
    
    while number > 0:
        list_of_bytes.append(32 + number % 64)
        number //= 64
    
    return bytes(reversed(list_of_bytes)).decode("ASCII")


def encode(string):
    str_len = len(string)

    list_of_symbols = list(reversed(sorted(list((j, i) for i, j in Counter(string).most_common()))))
    dictionary_of_codes = dict(list((list_of_symbols[i][1], "1" * i + "0") for i in range(len(list_of_symbols))))
    
    bit_string = "".join(dictionary_of_codes[i] for i in string)
    bit_string += "0" * (ceil(len(bit_string) / 6) * 6 - len(bit_string))
    
    return (str_len, "".join(dictionary_of_codes.keys()), shex(int(bit_string, 2)).strip())

def decode(str_len, code, coded_string):
    dictionary_of_codes = dict(list(("1" * i + "0", code[i]) for i in range(len(code))))
    string_list_of_codes = (str(bin(xehs(coded_string)))[2:] + "0").replace("0", "0 ").split()[:str_len]
    decoded_string = "".join(dictionary_of_codes[i] for i in string_list_of_codes)
    

    return decoded_string
