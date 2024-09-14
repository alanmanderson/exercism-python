def can_chain(dominoes):
    # validate a valid solution exists:
    counts = {}
    for d in dominoes:
        counts[d[0]] = counts.get(d[0], 0) + 1
        counts[d[1]] = counts.get(d[1], 0) + 1
    for key, value in counts.items():
        if value % 2 != 0:
            return None
    # pop the first domino
    domino = dominoes.pop(0)
    return max_chain_helper([domino], dominoes)
    # Check to see if it matches either side of the chain
    # if it matches put it on if it doesn't push it to the end

def max_chain_helper(chain, dominoes):
    if len(

def flip(domino):
    return (domino[1], domino[0])
