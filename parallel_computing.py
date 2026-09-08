# Demonstrates PARALLEL / CONCURRENT PROCESSING:
# multiple tasks start together and run at the same time instead of waiting for each other to finish.

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def task(n, duration=0.5):
    """Simulate one unit of work (e.g. an I/O call or computation)."""
    print(f"[Task {n}] started ...", flush=True)
    time.sleep(duration)                    # simulate real work
    result = f"result of task {n}"
    print(f"[Task {n}] finished -> {result}", flush=True)
    return result


def main():
    start = time.perf_counter()

    print("--- Parallel Computing Demo (ThreadPoolExecutor) ---\n")

    # Submit all 4 tasks at once; they run concurrently
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(task, i): i for i in range(1, 5)}

        # Results are collected as each task completes
        results = []
        for future in as_completed(futures):
            results.append(future.result())

    elapsed = time.perf_counter() - start
    print(f"\nAll tasks done. Total time: {elapsed:.2f} seconds")
    print("(Sequential equivalent would take ~2.00 seconds)")
    print(f"Results: {sorted(results)}")


if __name__ == "__main__":
    main()
