def latest(scores):
    return scores[-1]


def personal_best(scores):
    best = None
    for score in scores:
        if best is None or score > best:
            best = score
    return best


def personal_top_three(scores):
    best = scores[:3]
    best.sort(reverse = True)
    for score in scores[3:]:
        if score > best[2]:
            best[2] = score
            best.sort(reverse = True)
    return best
