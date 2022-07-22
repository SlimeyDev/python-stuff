from multiprocessing import Pool
from multiprocessing import cpu_count
import random

def f(x):
    while True:
        cal = x**x
        print(cal)

if __name__ == '__main__':
    processes = cpu_count()
    print('utilizing %d cores\n' % processes)
    pool = Pool(processes)
    pool.map(f, range(processes))