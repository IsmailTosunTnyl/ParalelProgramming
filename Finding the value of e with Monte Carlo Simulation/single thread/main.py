from it import *

# check github for latest version
# https://github.com/IsmailTosunTnyl/ParallelProgramming

if __name__ == '__main__':
    find_e = FindE()
    clock = TicToc()

    n = 100000000

    clock.tic()
    e = find_e.calculate_e(n)

    print("e = %12.7f | counter = %d | N = %d" %
          (e, find_e.counter, find_e.n))
    print("TIME = %.6f seconds" % (clock.toc()))
