alph_1 = set()
alph_2 = set()

def process_str(string, alph):
    for ch in string:
        alph.add(ch)

flg = True
while True:
    string = input()
    
    if len(string) == 0:
        break

    process_str(string, alph_1 if flg else alph_2)
    flg = not flg

if len(alph_1) > len(alph_2):
    print("Mumbo")
else:
    print("Jumbo")
