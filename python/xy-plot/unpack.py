from __future__ import print_function
from sys import argv, stdin, stderr
from collections import deque
from itertools import repeat

import wave, struct
import matplotlib.pyplot as plt

if argv[1] is '-':
    wav = wave.open(stdin, 'r')
else:
    wav = wave.open(argv[1], 'r')

while True:
    waveData = wav.readframes(1)
    if not waveData: break
    if wav.getnchannels() == 1:
        print("Not a stereo wave file.",file=stderr)
        break
    elif wav.getnchannels() == 2:
        data = struct.unpack("<hh", waveData)
        print(str(data[0])+','+str(data[1]))
