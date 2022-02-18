# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import matplotlib.pyplot as plt

from brutforce import brutforce
from heuristic import heuristic

MIN_SPEED = 0.1
MIN_LEN = 0.1
MIN_JOBS = 1
MIN_MACHINES = 1
MIN_BLOCKS = 1


def generate(n, m, Jmax, Smax, blocks=None):
    n_ = random.randint(MIN_JOBS, n)
    m_ = random.randint(MIN_MACHINES, m)

    if blocks == None:
        blocks = random.randint(MIN_BLOCKS, n_)

    J = []  # set of blocks of jobs
    M = []  # set of machine speeds

    count = n_
    # generate job blocks
    for i in range(blocks):
        jobs_in_block = random.randint(1, min(count - blocks + i + 1,
                                              m_))  # each block consists of at least one job but no more than the num of machines
        count -= jobs_in_block
        B = []
        for j in range(jobs_in_block):
            job = random.uniform(MIN_LEN, Jmax)
            B.append(job)

        J.append(B)

    n_ -= count

    # generate machine speeds
    for i in range(m_):
        speed = random.uniform(MIN_SPEED, Smax)
        M.append(speed)

    return n_, m_, J, M


def test(n, m, J, M):
    print()
    print(n)
    print(m)
    print(J)
    print(M)
    print()

    b = brutforce(n, m, J, M)
    h = heuristic(n, m, J, M)

    return b, h


def main():
    # print("ENTER: maximum number of jobs(int)")
    # n = int(input())
    #
    # print("ENTER: maximum number of machines(int)")
    # m = int(input())
    #
    # print("ENTER: maximum job size(float)")
    # Jmax = float(input())
    #
    # print("ENTER: maximum machine speed(float)")
    # Smax = float(input())
    #
    # print("ENTER: number of tests(int)")
    # tests = int(input())

    n = 10
    m = 4
    Jmax = 10
    Smax = 4
    tests = 50

    B = []
    H = []

    OX = [i for i in range(tests)]

    for _ in range(tests):
        n_, m_, J, M = generate(n, m, Jmax, Smax)
        b, h = test(n_, m_, J, M)
        B.append(b)
        H.append(h)

    RATIO = [B[i] / H[i] for i in range(tests)]

    print("Brutforce to heuristic average ratio: ", sum(RATIO) / len(RATIO))

    # GRAPH
    plt.plot(OX, B, label="brutforce")
    plt.plot(OX, H, label="heuristic")
    plt.title("Q|cliques|C_max brutforce to heuristic comparison")
    plt.xlabel("test")
    plt.ylabel("C_max")
    plt.legend()

    plt.show()


if __name__ == '__main__':
    main()
