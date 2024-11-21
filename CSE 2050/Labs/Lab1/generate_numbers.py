# This program generates a list of numbers and writes them to a file.
import random

##### Generate list of numbers #####
n = 1000 # Max is 2000 due to memory constraints with quicksort
L = [random.randint(0, n) for i in range(n)]

##### Create file to write to #####
f = open(f"./numbers.txt", "w")

##### Write numbers to file #####
for item in L:
    f.write(str(item))
    f.write(" ")

#### Close the file ####
f.close()
