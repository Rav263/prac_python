def statcounter():
    stats = dict()
    fun = yield stats
    
    while True:
        def new_fun(*args, fun = fun):
            stats.setdefault(fun, 0)
            stats[fun] += 1
            return fun(*args)
        fun = yield new_fun

