import time
import random

best_time = None
for _ in range(5):

    time.sleep(random.randrange(2, 5))

    Start_time = time.monotonic()
    input ("go!")
    end_time = time.monotonic()

    speed = end_time - Start_time

    print(speed)
    if best_time is None:
        best_time = speed
    if speed < best_time:
        best_time = speed
print(f"your fastest time is")








