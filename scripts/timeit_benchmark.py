import timeit
import functools

# Basic timing
def basic_timing():
    code = "sum(range(100))"
    t = timeit.timeit(code, number=10000)
    print(f"Basic: {t:.6f}s")

# Compare functions
def compare_funcs():
    def list_comp(): return [x**2 for x in range(100)]
    def map_func(): return list(map(lambda x: x**2, range(100)))
    
    funcs = [list_comp, map_func]
    for f in funcs:
        t = timeit.timeit(f, number=1000)
        print(f"{f.__name__}: {t:.6f}s")

# With setup code
def with_setup():
    setup = "import random; data = [random.randint(1,100) for _ in range(1000)]"
    code = "sorted(data)"
    t = timeit.timeit(code, setup=setup, number=100)
    print(f"Sort: {t:.6f}s")

# Repeat for accuracy
def repeat_timing():
    code = "'-'.join(str(n) for n in range(100))"
    times = timeit.repeat(code, repeat=5, number=1000)
    avg_t = sum(times) / len(times)
    print(f"Avg: {avg_t:.6f}s, Min: {min(times):.6f}s")

# Context manager approach
class Timer:
    def __enter__(self):
        self.start = timeit.default_timer()
        return self
    
    def __exit__(self, *args):
        self.end = timeit.default_timer()
        self.time = self.end - self.start
        print(f"Elapsed: {self.time:.6f}s")

# Usage examples
if __name__ == "__main__":
    basic_timing()
    compare_funcs()
    with_setup()
    repeat_timing()
    
    # Context manager
    with Timer():
        sum(x**2 for x in range(10000))