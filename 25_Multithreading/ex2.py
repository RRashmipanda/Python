import time
import threading

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

t1 = threading.Thread(target=cal_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))
 
t1.start()
t2.start()

t1.join() # means wait until this thread is completely executed
t2.join()
print("Done in: ", time.time()-t)

# Note: You can see that the total time taken is almost half of the previous example because both functions are running in parallel.
# like in sleep time of sqaure function, the cube function is also executing.

