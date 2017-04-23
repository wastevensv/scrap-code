from __future__ import print_function
from sys import argv, stdin, stderr
from collections import deque
from itertools import repeat

import matplotlib.pyplot as plt

try:
    input = raw_input
except NameError:
    pass

buflen=100

rd = deque(range(buflen),maxlen=buflen)
ld = deque(list(repeat(0,buflen)),maxlen=buflen)

if argv[1] is '-':
    file = stdin
else:
    file = open(argv[1], 'r')

plt.ion()
fig = plt.figure()
ln, = plt.plot([],[], 'ro')

while True:
    data = file.readline().split(',')
    if len(data) == 2:
        ld.append(data[0])
        rd.append(data[1])
    else:
        break
    ln.set_xdata(rd)
    ln.set_ydata(ld)
    plt.gca().relim()
    plt.gca().autoscale_view()
    plt.draw()
    plt.pause(0.1)
