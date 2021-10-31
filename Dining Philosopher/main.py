import os
import random
import time
from table import Table
from threading import Thread, Lock

from philosopher import Philosopher


# check github for latest version
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


def print_table(philosophers, locked_chopsticks):
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


def table_print(philosophers, main_coordinates, t, locked_chopsticks):
    table = t.table
    for i in range(len(philosophers)):
        table[main_coordinates[i][0]][main_coordinates[i][1]] = philosophers[i].eatingStatus
        table[main_coordinates[i][0]][main_coordinates[i][1] - 1] = philosophers[i].leftChopstick
        table[main_coordinates[i][0]][main_coordinates[i][1] + 1] = philosophers[i].rightChopstick
        table[main_coordinates[i][0] + 1][main_coordinates[i][1]] = str(philosophers[i].mealSize)

    for line in table:
        print(' '.join(line))
    print(f"""Eating Counter: {Philosopher.eatingCount}  Total size of meals left:{Philosopher.totalMealSize} 
             Locked Chopsticks: {locked_chopsticks}  """)


def main():
    philosopher_size = int(input("Philosopher size\n"))
    meal_size_perphilosopher = int(input("Meal size per philosopher\n"))

    dining_philosophers = DiningPhilosophers(philosopher_size, meal_size_perphilosopher)
    philosophers = [Thread(target=dining_philosophers.philosopher, args=(i,)) for i in range(philosopher_size)]

    t = Table(len(philosophers))
    main_coordinates = t.choosen_coordinats()

    for philosopher in philosophers:
        philosopher.start()

    while Philosopher.totalMealSize > 0:

        locked_chopstick_counter = 0
        for philosopher in dining_philosophers.philosophers:
            if philosopher.lock.locked():
                locked_chopstick_counter += 1

        # print_table(dining_philosophers.philosophers, locked_chopstick_counter)
        table_print(dining_philosophers.philosophers, main_coordinates, t, locked_chopstick_counter)

        time.sleep(0.1)
        os.system('cls')

    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main()
