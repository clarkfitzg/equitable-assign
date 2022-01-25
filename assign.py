'''
Idea for a talk:
    What do you think is more equitable?

    1. _Independent_ random assignment of K reviewers to each application.
    2. Balancing the work by randomly assigning each reviewer the same number
       of applications.
'''


from collections import Counter
import itertools
import math
import random


def assign(A: int, N: int, K: int, seed=None, verbose=True) -> list:
    """
    Assign N reviewers to A applications as equitably as possible, meaning
    the conditions below hold.

    Variables (all positive integers):
        - A applications
        - N reviewers
        - K reviewers look at each application

    1. Each application gets reviewed the same number of times (exactly K times).
    2. Each application is equally likely to be reviewed by every combination of
       reviewers.
    3. Each reviewer has the same number of applications to review (+/- 1).
       This means the workload will be even, and each reviewer is equally
       important.
    4. Each combination of reviewers appears as many times as every other
       combination of reviewers (+/- 1). This means that a particular combination
       of reviewers won't have a stronger or weaker voice compared to any other
       combination.
    """
    random.seed(seed)

    reviewers = range(1, N+1)

    n_each_combo, Aremain = divmod(A, math.comb(N, K))

    combos = list(itertools.combinations(reviewers, K))
    result = n_each_combo * combos

    remaining = assign_remaining(Aremain, N, K)
    result.extend(remaining)
    random.shuffle(result)

    workload = Counter(itertools.chain(*result))
    combo_counts = set(Counter(result).values())

    if not optimal(result):
        raise RuntimeError("Algorithm failed to satisfy optimality conditions.")

    if verbose:
        print(f'Each reviewer has {set(workload.values())} assignments',
              f'and each combination of {K} reviewers has {combo_counts}',
              "assignments. The work is randomly balanced.")

    return result


def assign_remaining(A: int, N: int, K: int, verbose=True) -> list:
    """
    Assign work when A < (N choose K)

    We only need to consider the case when the number of combinations is less than
    the number of remaining applications, since for every multiple of the number of
    combinations we can just randomly assign all the combinations and we'll have
    exact balance.

    The problem is to partition all possible combinations into two sets, one with A
    elements and a balanced workload. Balanced workload means that for the assigned
    set, each individual appears in the same number of combinations as every other
    other individual, +/- 1.

    The idea of this approach (my 4th), is to:
        1. randomly select A random combinations.
        2. trade combinations from the included set into the excluded set such that
           each trade improves the workload balance.
        3. Iterate the trading until balance is achieved.

    """
    if A == 0:
        return []

    reviewers = range(1, N+1)

    allcombos = [frozenset(x) for x in itertools.combinations(reviewers, K)]

    index = range(len(allcombos))
    keep = set(random.sample(index, A))
    nokeep = set(index).difference(keep)

    include = {allcombos[i] for i in keep}
    exclude = {allcombos[i] for i in nokeep}
    workload = Counter(itertools.chain(*include))

    # It's possible that some reviewers weren't assigned any.
    for r in reviewers:
        workload[r] += 0

    while counts_off(workload):
        incombo, outcombo = fast_trade(include, exclude, workload)
        include.discard(outcombo)
        exclude.add(outcombo)
        exclude.discard(incombo)
        include.add(incombo)
        for i in incombo:
            workload[i] += 1
        for i in outcombo:
            workload[i] -= 1

    return [tuple(sorted(c)) for c in include]


def fast_trade(include, exclude, workload):
    """
    Make the first good trade we find to improve the balance of the workload.

    We trade a combination with the most load for one with the smallest load.
    """
    workorder = workload.most_common()
    over = workorder[0][0]
    under = workorder[-1][0]

    for combo in include:
        #if over in combo and under not in combo:
        if over in combo:
            outcombo = combo

    for combo in exclude:
        #if under in combo and over not in combo:
        if under in combo:
            incombo = combo

    return incombo, outcombo


def best_trade(include, exclude, workload):
    """
    Make the best possible trade of one combination between include and exclude
    to improve the balance of the workload.

    We can understand this as finding the most loaded combination of workers
    and replacing it with the least loaded.
    """
    score = lambda x: sum(workload[i] for i in x)
    outcombo = max(include, key=score)
    incombo = min(exclude, key=score)

    return incombo, outcombo


def optimal(assignments):
    """
    Test assignments for optimal workload and combinations.
    """
    combos = Counter(assignments)
    workload = Counter(itertools.chain(*assignments))

    if counts_off(combos) or counts_off(workload):
        return False
    else:
        return True


def counts_off(d):
    """
    Is the count off by more than 1?
    """
    mx = max(d.values())
    mn = min(d.values())
    return 1 < mx - mn


if __name__ == "__main__":

    assign(6, 5, 2)

    assign(10, 5, 2)

    a = assign(110, 12, 3)

    b = assign(323, 5, 2, seed=123)

    # First this worked instantly, now it takes time?

#
#    math.comb(15, 5)
#

#    %time c = assign(999, 15, 5, seed=8023)
#

#    %time c = assign(999, 15, 5)

# Seems to cause a cycle.
#    %time c = assign(999, 15, 10, seed=130)

# While this one works fine:
#%time c = assign(999, 15, 10, seed=1090)


#    %time c = assign(999, 16, 10, seed=130)
#
#    time c = assign(999, 20, 10, seed=130)

#
#    %time c = assign(999, 15, 5)
