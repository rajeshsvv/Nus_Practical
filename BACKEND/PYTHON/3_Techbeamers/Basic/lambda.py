from functools import reduce

def fn(m, n) : return m + n

print(reduce((lambda m, n: m + n), [1, 2, 3, 4]))
print(reduce(fn, [1, 2, 3, 4]))

import time

start=time.time()
print("It is in some module")
time.sleep(.1)
end=time.time()
print(end-start)


import time

template = 'time()# {:0.2f}, clock()# {:0.2f}'

print(template.format(time.time(), time.perf_counter()))

for i in range(3, 0, -1):
 print('>Sleeping for', i, 'sec.')
 time.sleep(i)
 print(template.format(time.time(), time.perf_counter()))

 # print(help(list))
