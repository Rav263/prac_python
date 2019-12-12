dictionary = dict()

while True:
    try:
        now_str = input()
        if now_str == ".":
            break
        if now_str[0] == "#":
            continue
        if "=" in now_str:
            some = now_str.split("=")
            if len(some) >= 3:
                print("invalid assignment '" + now_str +"'")
                continue
            try:
                exec(now_str, dictionary)
                continue
            except Exception as e:
                print("invalid identifier '"+some[0]+"'")
                continue

        try:
            print(eval(now_str, dictionary))
        except Exception as e:
            print(str(e))
    except Exception:
        break
