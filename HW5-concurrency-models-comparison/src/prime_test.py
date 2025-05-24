import threading
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count, freeze_support
import matplotlib.pyplot as plt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def run_manual_threads(numbers):
    threads = []
    start = time.time()
    for n in numbers:
        t = threading.Thread(target=is_prime, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    return end - start

def run_executor_threads(numbers, max_workers=10):
    start = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        list(executor.map(is_prime, numbers))
    end = time.time()
    return end - start

def run_multiprocessing(numbers, num_processes=None):
    if num_processes is None:
        num_processes = cpu_count()
    start = time.time()
    with Pool(processes=num_processes) as pool:
        pool.map(is_prime, numbers)
    end = time.time()
    return end - start

if __name__ == '__main__':
    freeze_support() 

    workloads = [50, 100, 200, 400, 800, 1600, 3000, 6000, 10000,20000, 35000, 50000]
    manual_times = []
    executor_times = []
    multiprocessing_times = []

    for count in workloads:
        numbers = list(range(10_000, 10_000 + count))
        manual_times.append(run_manual_threads(numbers))
        executor_times.append(run_executor_threads(numbers))
        multiprocessing_times.append(run_multiprocessing(numbers))

    plt.figure(figsize=(10, 6))
    plt.plot(workloads, manual_times, marker='o', label='Manual Threading')
    plt.plot(workloads, executor_times, marker='s', label='ThreadPoolExecutor')
    plt.plot(workloads, multiprocessing_times, marker='^', label='Multiprocessing')
    plt.title('Performance Comparison of Threading Models')
    plt.xlabel('Number of Tasks (Prime Checks)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
