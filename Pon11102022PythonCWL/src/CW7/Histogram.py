import matplotlib.pyplot as plt
import numpy as np
import psutil
from concurrent.futures import ThreadPoolExecutor

def histogram():
    for i in range(10):
        x = np.random.normal(200, 10, 1000)
        plt.hist(x)
        plt.show()

def cpu_times():
    for i in range(20):
        print(psutil.cpu_times_percent(interval = 1))

def main():
    with ThreadPoolExecutor() as exe:
        exe.submit(cpu_times)
        exe.submit(histogram)

if __name__ == '__main__':
    main()
