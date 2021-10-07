from it import *
from threading import Thread

if __name__ == '__main__':
    find_e = FindE()
    clock = TicToc()

    n = 10000000

    clock.tic()
    Thread(target=find_e.throw_points, args=(n,)).start()

    print("e = %12.7f | counter = %d | N = %d" %
          (find_e.calculate_e(), find_e.counter, find_e.n))
    print("TIME = %.6f seconds" % (clock.toc()))
