import time
import os

count = 1
start = time.time()
while True:
    count += 1
    if count == 100000000:
        break

end = time.time()
print(start)
print(end)
print(end - start)

    