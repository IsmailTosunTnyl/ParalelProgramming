import time
import random



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

        for _ in range(nn):
            self.n += 1
            sum = 0
            while True:
                sum = sum + random.random()
                self.counter += 1
                if sum >= 1:
                    break

    def calculate_e(self):
        return self.counter / self.n
