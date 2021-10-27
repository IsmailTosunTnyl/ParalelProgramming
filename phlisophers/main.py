import random
import time
from threading import Thread, Lock
from philosopher import Philosopher


class DiningPhilosophers:
    def __init__(self, number_of_philosopher, meal_size):

        # self.meals = [meal_size for _ in range(number_of_philosopher)]
        # self.chopsticks = [Lock() for _ in range(number_of_philosopher)]
        # self.status = ['T' for _ in range(number_of_philosopher)]
        self.philosophers = [Philosopher(meal_size, Lock()) for i in range(number_of_philosopher)]

    def philosopher(self, i):
        while self.philosophers[i].mealSize > 0:

            # self.status[i] = 'T'
            j = (i + 1) % 5

            time.sleep(random.random())
            if not self.philosophers[i].lock.locked():
                self.philosophers[i].set_left_chopstick(True)
                self.philosophers[i].lock.acquire()

                time.sleep(random.random())
                if self.philosophers[j].lock.locked():
                    self.philosophers[i].set_left_chopstick(False)
                    self.philosophers[i].lock.release()

                else:
                    self.philosophers[i].set_right_chopstick(True)
                    self.philosophers[j].lock.acquire()

                    # self.status[i] = 'E'
                    # self.meals[i] -= 1
                    time.sleep(random.random())
                    self.philosophers[j].lock.release()
                    self.philosophers[i].set_right_chopstick(False)

                    self.philosophers[i].lock.release()
                    self.philosophers[i].set_left_chopstick(False)

                    # self.status[i] = 'T'


def main():
    n = 5
    m = 10
    dining_philosophers = DiningPhilosophers(n, m)
    philosophers = [Thread(target=dining_philosophers.philosopher, args=(i,)) for i in range(n)]
    for philosopher in philosophers:
        philosopher.start()
    while Philosopher.totalMealSize > 0:
        # print(dining_philosophers.status, str(dining_philosophers.status.count('E')), dining_philosophers.meals)
        for p in dining_philosophers.philosophers:
            print(p, end="")
        print(" Easting Count: ", Philosopher.eatingCount, " Total Meal size", Philosopher.totalMealSize)

        time.sleep(0.1)
    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main()
