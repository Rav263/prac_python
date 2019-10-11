def maxfun(S, *funs):
    return funs[max((sum(fun(i) for i in S), ind) for ind, fun in enumerate(funs))[1]]
