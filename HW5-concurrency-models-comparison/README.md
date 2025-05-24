# Python Concurrency Performance Comparison

## Overview

This project benchmarks and compares the performance of three different concurrency models in Python:

1. **Manual Threading** using `threading.Thread`
2. **ThreadPoolExecutor** from the `concurrent.futures` module
3. **Multiprocessing** using `multiprocessing.Pool`

The experiments measure how each model performs in executing both lightweight and heavy CPU-bound tasks under increasing load.

---

## Tasks Evaluated

### 1. Prime Check (Lightweight Task)
- Checks whether a given integer is prime.
- Represents a simple, easily parallelizable task.

### 2. Recursive Fibonacci (Heavy CPU-bound Task)
- Calculates Fibonacci numbers using a naive recursive algorithm (`fib(n)`).
- Simulates compute-intensive workloads to stress concurrency behavior.

---

## Purpose

The main goal of this project is to:

- Understand how Python’s concurrency mechanisms behave under different workloads.
- Analyze the impact of the **Global Interpreter Lock (GIL)** on `threading` and `ThreadPoolExecutor`.
- Explore how `multiprocessing` can achieve real parallelism in CPU-bound scenarios.

---

## Project Structure

```
├── report.pdf             # Full report with explanations, charts, and analysis
├── src/
│   ├── prime_test.py                    # Code for the prime number benchmark
│   └── fibonacci_test.py                # Code for the recursive Fibonacci benchmark
└── README.md
```

---

## How to Run the Code

### Requirements

This project is based on Python 3.8+ and uses only standard libraries.

### Run Benchmarks

You can run the benchmark scripts directly using Python:

```bash
python src/prime_test.py
python src/fibonacci_test.py
```

Each script will execute the tasks using the three concurrency models and plot execution times using `matplotlib`.

---

## Key Observations

- **Manual Threading** suffers from high overhead as the number of threads increases.
- **ThreadPoolExecutor** performs well in lightweight tasks due to task queuing and thread reuse.
- **Multiprocessing** is the only model that bypasses the GIL and achieves real parallelism in CPU-bound tasks.
