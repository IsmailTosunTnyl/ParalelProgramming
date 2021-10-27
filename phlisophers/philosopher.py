class Philosopher():
    eatingCount = 0
    totalMealSize = 0

    def __init__(self, meal_size,lock):
        Philosopher.totalMealSize += meal_size
        self.rightChopstick = " "
        self.leftChopstick = " "
        self.eatingStatus = "T"
        self.mealSize = meal_size
        self.lock = lock

    def set_eating_philosopher_count(self):

        if self.eatingStatus == "E":
            Philosopher.eatingCount += 1
        else:
            Philosopher.eatingCount -= 1

    def set_eating_status(self):
        temp_status = self.eatingStatus
        if self.rightChopstick == "-" and self.leftChopstick == "-":
            self.eatingStatus = "E"
            self.mealSize -= 1
            Philosopher.totalMealSize -= 1

        else:
            self.eatingStatus = "T"

        if temp_status != self.eatingStatus:
            self.set_eating_philosopher_count()

    def set_right_chopstick(self, n):
        if n:
            self.rightChopstick = "-"
        else:
            self.rightChopstick = " "

        self.set_eating_status()

    def set_left_chopstick(self, n):
        if n:
            self.leftChopstick = "-"
        else:
            self.leftChopstick = " "

        self.set_eating_status()

    def __str__(self):
        return self.leftChopstick + self.eatingStatus + self.rightChopstick +" meal: "+str(self.mealSize)+" "


if __name__ == "__main__":
    p = Philosopher(10)

    print(p)
    p.set_left_chopstick(True)
    print(p)
    p.set_right_chopstick(True)
    print(Philosopher.eatingCount)
    print(p)
    p.set_right_chopstick(False)
    print(p)
    print(Philosopher.eatingCount)
