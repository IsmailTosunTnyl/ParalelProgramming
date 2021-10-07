from it import *

if __name__ == '__main__':
    find_e = FindE()
    clock = TicToc()

    n = 10000000

    clock.tic()
    e = find_e.throw_points(n)

    print("e = %12.7f | counter = %d | N = %d" %
          (e, find_e.counter, n))
    print("TIME = %.6f seconds" % (clock.toc()))
