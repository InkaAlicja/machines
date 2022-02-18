def cmax(n, m, J, M, mask):
    t = [0] * m

    for i in range(n):
        t[mask[i]] += J[i] / M[mask[i]]

    res = t[0]
    for sum in t:
        res = max(res, sum)

    return res


# add one to a number of length n in the positional numerical system with base m,
# where <mask> is the numbers representation in that system
def add_one(n, m, mask):
    i = 0
    while i < n:
        if mask[i] < m - 1:
            mask[i] += 1
            return True
        else:
            mask[i] = 0
        i += 1

    return False


# check if no two jobs from the same block(clique) are assigned to the same machine
def feasible(mask, J, m):
    job_it = 0
    for b in J:
        used = [False] * m
        for job in b:
            if used[mask[job_it]]:
                return False
            else:
                used[mask[job_it]] = True

            job_it += 1
    return True


def brutforce(n, m, J, M):
    J_flat = [job for block in J for job in block]
    mask = [0] * n

    best = cmax(n, m, J_flat, M, mask)
    best_assign = mask

    while add_one(n, m, mask):
        # best = min(best, cmax(n, m, J_flat, M, mask))
        if feasible(mask, J, m) and best > cmax(n, m, J_flat, M, mask):
            best = cmax(n, m, J_flat, M, mask)
            best_assign = mask.copy()

    print("\nbrut:")
    print("jobs of lengths")
    print(J_flat)
    print("get assigned to machines ==>")
    print(best_assign)
    print(best)
    return best
