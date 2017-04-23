from __future__ import print_function
from sys import argv, stdin, stderr
from collections import deque
from itertools import repeat

import wave, struct
import matplotlib.pyplot as plt

buflen=100

rd = deque(range(buflen),maxlen=buflen)
ld = deque(list(repeat(0,buflen)),maxlen=buflen)
def unpack(wav):
    waveData = wav.readframes(1)
    if not waveData: return False
    if wav.getnchannels() == 1:
        data = struct.unpack("<h", waveData)
        ld.append(data[0])
    elif wav.getnchannels() == 2:
        data = struct.unpack("<hh", waveData)
        ld.append(data[0])
        rd.append(data[1])
    return True


if len(argv) is 1 or argv[1] is '-':
    waveFile = wave.open(stdin, 'r')
else:
    waveFile = wave.open(argv[1], 'r')

plt.ion()
fig = plt.figure()
ln, = plt.plot([],[], 'ro')
active = True
while active:
    active = unpack(waveFile)
    plt.pause(0.00001)
    ln.set_xdata(rd)
    ln.set_ydata(ld)
    plt.gca().relim()
    plt.gca().autoscale_view()
    plt.draw()
