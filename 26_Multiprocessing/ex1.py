# multiprocessing in python means running multiple processes at the same time
# each process has its own memory space
# multiprocessing is used to bypass the GIL (Global Interpreter Lock) in python
# multiprocessing is used to run CPU bound tasks in parallel


import time
import multiprocessing


sqaure_result = []

def calc_square(numbers):
    global sqaure_result
    for n in numbers:
        print("square ", n * n)
        sqaure_result.append(n * n)
    print("inside process ", sqaure_result)

# def calc_cube(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print("cube ", n * n * n)



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    # p2 = multiprocessing.Process(target=calc_cube, args=(arr,))


    p1.start()
    p1.join()
  
    print("result ", sqaure_result)
    print("Done !")

    # result is empty because each process has its own memory space
    # to share data between processes we can use multiprocessing.Queue or multiprocessing.Pipe
    