# how to calculate execution time in python

import time

# performance counter method will return arbitrary moment in time
start_time = time.perf_counter()

# how long would 100 million iterations take?
for i in range(100000000):
    pass

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"elapsed time: {elapsed_time:.1f} seconds")