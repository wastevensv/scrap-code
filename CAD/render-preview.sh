#!/bin/sh
d=$(basename `pwd`)
FRAMES=60
DIST=100

Xvfb :1 -screen 0 800x600x24 &
export DISPLAY=:1
openscad -o $d.png --camera=$DIST,0,$DIST,0,0,0 $d.scad 2>$d.log
pkill Xvfb
