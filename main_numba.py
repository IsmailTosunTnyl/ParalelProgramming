from it_numba import *

if __name__ == '__main__':
    for _ in range(3):
        find_e = FindE()
        clock = TicToc()

        n = 10000000

        clock.tic()
        find_e.throw_points(n)

        print("e = %12.7f | counter = %d | N = %d" %
              (find_e.find_euler(), find_e.counter, find_e.n))
        print("TIME = %.6f seconds" % (clock.toc()))
