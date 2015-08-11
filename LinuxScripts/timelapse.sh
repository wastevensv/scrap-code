#!/bin/bash

while true; do
  fswebcam -S 120 -r 800x600 --save `date +%d_%H%m%S`.jpg # take photo, filename is day_time
  for i in {600..1}; do echo $i; sleep 1; done # 600s countdown timer
done
