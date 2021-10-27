import pandas as pd
import numpy as np
import sys
import time
x = list()

import os

clear = lambda: os.system('cls')



n = 20
for _ in range(n):
    x.append([])

for i in x:
    for _ in range(200):
        i.append(".")


x[0][50] = "5"
for i in x:
    print(''.join(map(str, i)))

time.sleep(5)
clear()
