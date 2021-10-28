import os
import random
import time
from threading import Thread, Lock

from philosopher import Philosopher


# https://github.com/IsmailTosunTnyl/ParallelProgramming

class DiningPhilosophers:
    def __init__(self, number_of_philosopher, meal_size):

        self.philosophers = [Philosopher(meal_size, Lock()) for i in range(number_of_philosopher)]

    def philosopher(self, i):
        while self.philosophers[i].mealSize > 0:

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

                    time.sleep(random.random())
                    self.philosophers[j].lock.release()
                    self.philosophers[i].set_right_chopstick(False)

                    self.philosophers[i].lock.release()
                    self.philosophers[i].set_left_chopstick(False)


def print_table(philosophers,locked_chopsticks):
    print(f"""
    
              {philosophers[0]}
               {philosophers[0].mealSize}
                 
   
    {philosophers[4]}                    {philosophers[1]}
     {philosophers[4].mealSize}                      {philosophers[1].mealSize}
     
        
        {philosophers[3]}           {philosophers[2]}                 
         {philosophers[3].mealSize}            {philosophers[2].mealSize}
         
 Eating Counter: {Philosopher.eatingCount}  Total size of meals left:{Philosopher.totalMealSize} 
             Locked Chopsticks: {locked_chopsticks}   
    """)


def main():
    n = 5
    m = 10

    dining_philosophers = DiningPhilosophers(n, m)
    philosophers = [Thread(target=dining_philosophers.philosopher, args=(i,)) for i in range(n)]
    for philosopher in philosophers:
        philosopher.start()

    while Philosopher.totalMealSize > 0:

        locked_chopstick_counter = 0
        for philosopher in dining_philosophers.philosophers:
            if philosopher.lock.locked():
                locked_chopstick_counter += 1

        print_table(dining_philosophers.philosophers,locked_chopstick_counter)

        time.sleep(0.1)
        os.system('cls')

    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main()
