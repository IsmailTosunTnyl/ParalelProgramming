import random
import math


class Table:

    def __init__(self, ph_count):
        self.ph_count = ph_count
        self.width = ph_count *2
        self.height = ph_count *2
        self.radius = ph_count -1
        self.center_x = ph_count -1
        self.center_y = ph_count -1
        self.table = list()


    def blank_table(self):

        self.table = [['.' for _ in range(self.width)] for _ in range(self.height)]
        return self.table

    def find_coordinates(self):

        coordinates = []

        # draw the circlefor angle in range(0, 360, 5):
        for angle in range(0, 360, 5):
            x = self.radius * math.sin(math.radians(angle)) + self.center_x
            y = self.radius * math.cos(math.radians(angle)) + self.center_y

            if [int(round(x)), int(round(y))] not in coordinates:
                coordinates.append([int(round(x)), int(round(y))])
                # table[int(round(y))][int(round(x))] = '#'
        return coordinates

    def choosen_coordinats(self):
        self.table = self.blank_table()
        coordinates = self.find_coordinates()

        allocated_coordinates = []
        main_coordinates = []
        lock = 0
        while True:
            if lock > 500:
                print("houston we have a problem")
                allocated_coordinates = []
                main_coordinates = []
                self.table = self.blank_table()
                lock = 0
            lock += 1
            x, y = coordinates[random.randint(0, len(coordinates) - 1)]

            if [x, y] not in allocated_coordinates and x != 0 and y != 0:
                if [x + 1, y] not in allocated_coordinates and [x + 1, y - 1] not in allocated_coordinates:
                    if [x + 1, y + 1] not in allocated_coordinates and [x, y + 1] not in allocated_coordinates:
                        if [x + 1, y - 1] not in allocated_coordinates and [x - 1, y] not in allocated_coordinates:
                            if [x - 1, y + 1] not in allocated_coordinates and [x - 1,
                                                                                y - 1] not in allocated_coordinates:
                                main_coordinates.append([x, y])
                                allocated_coordinates.append([x, y])
                                allocated_coordinates.append([x + 1, y])
                                allocated_coordinates.append([x + 1, y - 1])
                                allocated_coordinates.append([x + 1, y + 1])
                                allocated_coordinates.append([x, y + 1])
                                allocated_coordinates.append([x + 1, y - 1])
                                allocated_coordinates.append([x - 1, y])
                                allocated_coordinates.append([x - 1, y + 1])
                                allocated_coordinates.append([x - 1, y - 1])

                                self.table[x][y] = '#'
                        # table[(len(table[0])-x)][len(table[0][0])-y] = '#'

            if len(main_coordinates) == self.ph_count:
                break
        print("aloocated", allocated_coordinates)
        return main_coordinates


if __name__ == "__main__":
    ph_count = 5

    # c = circle(10, 10, 4, 4, 4)
    c = Table(ph_count)
    main_coordinates = c.choosen_coordinats()
    table = c.table
    print("main", main_coordinates)

    for line in table:
        print(' '.join(line))

    s = [i for i in range(0, 21, 10)]
