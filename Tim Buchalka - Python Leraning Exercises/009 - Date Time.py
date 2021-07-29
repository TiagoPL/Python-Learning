import time
print()  # ================================================

print(time.gmtime(0))
print(time.localtime())
print(time.time())

print()  # ================================================

timeVAR = time.localtime()
print('Year:', timeVAR[0], timeVAR.tm_year)
print('Month:', timeVAR[1], timeVAR.tm_mon)
print('Day:', timeVAR[2], timeVAR.tm_mday)

print()  # ================================================

from time import perf_counter as my_timer
import random

input('Press enter to start')

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()

input('Press enter to stop')

end_time = my_timer()

print('Started as ' + time.strftime('%X', time.localtime(start_time)))
print('Ended at ' + time.strftime('%X', time.localtime(end_time)))
print(f'Your reaction time was {end_time - start_time} seconds')

print()  # ================================================

