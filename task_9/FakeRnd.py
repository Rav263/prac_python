last_args = tuple()
now = 0

def randrange(*args):
    global last_args, now
    if last_args != args:
        last_args = args
        now = 0 if len(args) == 1 else args[0]
        return now
    args = args[:-1] if len(args) == 4 else args
    now += args[2] if len(args) == 3 else 1
    now  = now % args[0] if len(args) == 1 else ((args[0] + (now - args[1]) if now >= args[1] else now) if args[2] > 0 else (args[0] - (args[1] - now) if now <= args[1] else now))
    return now
    

randint_counter = 0

def randint(a, b):
    global randint_counter
    randint_counter += 1
    return a if randint_counter % 2 == 1 else b
