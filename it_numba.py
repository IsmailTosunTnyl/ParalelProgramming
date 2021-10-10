import time
import random
from numba import jit


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindE:

    def __init__(self):
        self.counter = 0
        self.n = 0

    def throw_points(self, nn):

        self.n, self.counter = self.throw_points_static(nn)

    @staticmethod
    @jit
    def throw_points_static(nn):
        n = 0
        counter = 0
        for _ in range(nn):
            n += 1
            sum = 0
            while True:
                sum = sum + random.uniform(0, 1)
                counter += 1
                if sum >= 1:
                    break
        return n, counter

    def find_euler(self):
        return self.counter / self.n