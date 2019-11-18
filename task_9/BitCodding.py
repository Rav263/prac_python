from collections import Counter
from math import ceil


def xehs(s):
    a = []

    for c in s:
        d = ord(c)-32
        a.extend([chr(48+(d>>3)),chr(48+(d&7))])

    return int("".join(a), 8)

def shex(n):
    preoctal = oct(n)
    N = len(preoctal)
    
    octal = "0"*(N%2) + preoctal[2:]
    N = len(octal)

    a = []
    for i in range(0,N,2):
        d1 = ord(octal[i]) - 48
        d2 = ord(octal[i+1]) - 48
        a.append(chr(d1*8 + d2 + 32))

    return "".join(a)

def encode(string):
    str_len = len(string)

    list_of_symbols = list(reversed(sorted(list((j, i) for i, j in Counter(string).most_common()))))
    dictionary_of_codes = dict(list((list_of_symbols[i][1], "1" * i + "0") for i in range(len(list_of_symbols))))
    
    bit_string = "".join(dictionary_of_codes[i] for i in string)
    bit_string += "0" * (ceil(len(bit_string) / 6) * 6 - len(bit_string))
    
    index_of_one = bit_string.find("1")
    index_of_one += 6 - index_of_one % 6

    coded_string = "".join(" " if bit_string[i:i+6] == "000000" else shex(int(bit_string[i:i+6], 2)) for i in range(0, index_of_one, 6)) 
    coded_string += shex(int(bit_string[index_of_one:], 2))
    return (str_len, "".join(dictionary_of_codes.keys()), coded_string)

def decode(str_len, code, coded_string):
    dictionary_of_codes = dict(list(("1" * i + "0", code[i]) for i in range(len(code))))
    
    num_of_spaces = 0
    for i in coded_string:
        if i != " ":
            break
        num_of_spaces += 1
    
    string_list_of_codes = ((lambda x: "000000"*num_of_spaces+"0" * ((6 - len(x) % 6) % 6) + x)(str(bin(xehs(coded_string)))[2:])).split("0")[:-1][:str_len]
    decoded_string = "".join(dictionary_of_codes[i + "0"] for i in string_list_of_codes)

    return decoded_string
