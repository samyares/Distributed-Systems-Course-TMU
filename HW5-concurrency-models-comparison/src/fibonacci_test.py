import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count
import time
import matplotlib.pyplot as plt

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def run_manual_threads_fib(numbers):
    threads = []
    start = time.time()
    for n in numbers:
        t = threading.Thread(target=fib, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    return end - start

def run_executor_threads_fib(numbers, max_workers=10):
    start = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        list(executor.map(fib, numbers))
    end = time.time()
    return end - start

def run_multiprocessing_fib(numbers, num_processes=None):
    if num_processes is None:
        num_processes = cpu_count()
    start = time.time()
    with Pool(processes=num_processes) as pool:
        pool.map(fib, numbers)
    end = time.time()
    return end - start

if __name__ == '__main__':
    workloads = [5, 10, 15, 20, 25, 35, 60, 100, 135, 170, 250, 350,450,600]
    manual_times_fib = []
    executor_times_fib = []
    multiprocessing_times_fib = []

    for count in workloads:
        numbers = [25] * count  
        manual_times_fib.append(run_manual_threads_fib(numbers))
        executor_times_fib.append(run_executor_threads_fib(numbers))
        multiprocessing_times_fib.append(run_multiprocessing_fib(numbers))

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.plot(workloads, manual_times_fib, marker='o', label='Manual Threading (fib)')
    plt.plot(workloads, executor_times_fib, marker='s', label='ThreadPoolExecutor (fib)')
    plt.plot(workloads, multiprocessing_times_fib, marker='^', label='Multiprocessing (fib)')
    plt.title('Performance Comparison (CPU-Intensive Task: fib(25))')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
