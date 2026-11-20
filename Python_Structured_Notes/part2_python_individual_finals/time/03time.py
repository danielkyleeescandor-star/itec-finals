
import time

start = time.perf_counter()

for number in range(1, 1000001):
    pass

end = time.perf_counter()

execution_time = end - start

print("Program Finished!")
print("Execution Time:", execution_time, "seconds")
