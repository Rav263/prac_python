from collections import defaultdict

def checkhash(ran, fun_hash, mod):
    hashs = defaultdict(int)
    for i in ran:
        hashs[fun_hash(i) % mod] += 1

    return (max(hashs.values()), min(hashs.values()))
