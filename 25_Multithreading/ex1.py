# multithreading in python means running multiple threads (smaller units of a process) at the same time
# for given list of numbers print square and cube for every numbers


import time

def cal_square(numbers):
    print("Calculating squares")
    for n in numbers:
        time.sleep(0.5)  # simulating a time-consuming task
        print('square',n*n)

def calc_cube(numbers):
        print("Calculating cubes")
        for n in numbers:
            time.sleep(0.5)  # simulating a time-consuming task
            print('cube',n*n*n)

arr = [2,3,4]

t=time.time()
cal_square(arr)
calc_cube(arr)

print("Done in: ", time.time()-t)
