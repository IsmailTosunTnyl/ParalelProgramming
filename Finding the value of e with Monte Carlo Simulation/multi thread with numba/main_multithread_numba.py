from it_multithread_numba import *
from threading import Thread
import os

# check github for latest version
# https://github.com/IsmailTosunTnyl/ParallelProgramming
if __name__ == '__main__':
    for _ in range(3):
        clock = TicToc()
        clock.tic()

        n = 10000000
        find_es = []
        threads = []

        for i in range(os.cpu_count()):
            find_es.append(FindE())
            threads.append(Thread(target=find_es[i].calculate_e, args=(n,)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        n = 0
        counter = 0
        for find_e in find_es:
            n += find_e.n
            counter += find_e.counter

        print("e = %12.7f | counter = %d | N = %d" %
              (counter / n, counter, n))
        print("TIME = %.6f seconds" % (clock.toc()))
