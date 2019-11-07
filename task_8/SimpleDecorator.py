def nonify(fun):
    def new_fun(*args, **kwargs):
        result = fun(*args, **kwargs)
        if result == type(result)():
            return None
        return result

    return new_fun
