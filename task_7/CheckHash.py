def checkhash(ran, fun_hash, mod):
    hashs = dict()
    for i in ran:
        now_hash = fun_hash(i) % mod
        if now_hash not in hashs:
            hashs[now_hash] = 0

        hashs[now_hash] += 1

    return (max(hashs.values()), min(hashs.values()))
