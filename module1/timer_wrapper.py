import time


def timing_function(some_function):
    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        print("Time it took to run the function:" + str((t2-t1)) + "\n")
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in range(0, 10000):
        num_list.append(num)
    print("Sum is " + str(sum(num_list)))


if __name__ == "__main__":
    my_function()