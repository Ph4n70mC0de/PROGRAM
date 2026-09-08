# Demonstrates SEQUENTIAL PROCESSING:
# each step runs one at a time, in strict order, and later steps depend on the results of earlier ones.

import time


def step(n, description, duration=0.5):
    """Simulate one processing step."""
    print(f"[Step {n}] {description} ...", flush=True)
    time.sleep(duration)          # simulate real work
    result = f"result of step {n}"
    print(f"[Step {n}] Done -> {result}")
    return result


def main():
    start = time.perf_counter()

    print("--- Sequential Processing Demo ---\n")

    # Steps run strictly one after another: 1 -> 2 -> 3 -> 4
    r1 = step(1, "Reading input data")
    r2 = step(2, f"Validating {r1}")
    r3 = step(3, f"Transforming {r2}")
    r4 = step(4, f"Saving {r3} to database")

    elapsed = time.perf_counter() - start
    print(f"\nAll steps finished in order. Total time: {elapsed:.2f} seconds")
    print(f"Final output: {r4}")


if __name__ == "__main__":
    main()
