import time
import os

count = 1
start = time.time()
while True:
    count += 1
    if count == 1000000000:
        break

end = time.time()
print(end - start)

    