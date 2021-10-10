import time
import random
from numba import int32, float32  # import the types
from numba.experimental import jitclass


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


@jitclass(spec=[("counter", int32), ("n", int32)])
class FindE:

    def __init__(self):
        self.counter = 0
        self.n = 0

    def throw_points(self, nn):

        for _ in range(nn):
            self.n += 1
            sum = 0
            while True:
                sum = sum + random.uniform(0, 1)
                self.counter += 1
                if sum >= 1:
                    break

    def calculate_e(self):
        return self.counter / self.n
