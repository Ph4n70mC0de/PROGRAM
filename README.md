# Sequential vs. Parallel Processing Demo

A small Python project that demonstrates the difference between **sequential (one-at-a-time) processing** and **parallel (concurrent) processing** using Python's standard library.

## Files

| File                       | Description                                                                                                                                                 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sequential_processing.py` | Runs 4 steps strictly one after another (1 → 2 → 3 → 4). Each step depends on the result of the previous one. Takes roughly **2 seconds** total (4 × 0.5s). |
| `parallel_computing.py`    | Submits 4 independent tasks to a `ThreadPoolExecutor`, which run **at the same time**. Takes roughly **0.5 seconds** total instead of ~2 seconds.           |

## How to Run

Requires Python 3 (standard library only — no external dependencies).

```bash
python sequential_processing.py
python parallel_computing.py
```

## Expected Output

- **Sequential:** steps finish in order 1, 2, 3, 4; total time ≈ 2.00 seconds.
- **Parallel:** all 4 tasks start together and finish concurrently; total time ≈ 0.50 seconds (a 4× speedup for this I/O-style workload).

## Key Takeaway

When tasks are independent (especially I/O-bound work such as network calls or file reads), running them in parallel with threads can dramatically reduce total execution time. When tasks depend on each other's results, sequential processing is required.

## ⚠️ Notice: No Copying Allowed

Please **do not use or copy this code**. You need to **create your own** — **don't steal someone else's work.**

Copying and submitting this demo as your own is plagiarism. Use it only as a reference to understand the concepts (sequential vs. parallel processing), then write your own implementation from scratch.

