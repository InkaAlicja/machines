ACCURACY = 0.05

#find the least occupied machine(with the most free space)
def machine(space, job, used):
    index = -1

    for i in range(len(space)):
        if space[i] - job >= 0 and (index == -1 or space[i] > space[index]) and not used[i]:
            index = i

    return index


def heuristic(n, m, J, M):
    _mask = [0] * n

    # binsearch over possible Cmax:
    p = 0
    q = sum([job for block in J for job in block]) / min(M) + 1
    feasible = False
    while q - p > ACCURACY or not feasible:
        job_it = 0
        s = (q + p) / 2

        # for Cmax = s calculate space on each machine
        space = [M[i] * s for i in range(m)]

        feasible = True
        for b in J:
            # in descending order
            b.sort(reverse=True)

            # no two jobs from the same block(clique) can be assigned to the same machine
            used = [0] * m

            for job in b:
                # find the least occupied machine(with the most free space)
                index = machine(space, job, used)
                # if the job cannot be assigned to any machine there is no feasible schedule with makespan <= s
                if index == -1:
                    feasible = False
                    break
                else:
                    # otherwise assign the job to the least occupied machine
                    used[index] = True
                    space[index] -= job
                    _mask[job_it] = index
                    job_it += 1

        if feasible:
            q = s
        else:
            p = s

    # print("\nheura:")
    # print("jobs of lengths")
    # print([job for block in J for job in block])
    # print("get assigned to machines ==>")
    # print(_mask)
    # print(q)
    return q
