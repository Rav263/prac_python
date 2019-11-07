from math import *
def fix(n):
    def decor(fun):
        def new_fun(*args, **kwargs):
            result = fun(*tuple(round(i, n) if isinstance(i, float) else i for i in args), **dict((k, round(v, n) if isinstance(v, float) else v) for k,v in kwargs.items()))
            if isinstance(result, float):
                return round(result, n)
            return result
        return new_fun
    return decor

