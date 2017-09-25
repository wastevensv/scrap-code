#!/bin/sh
# Creates an animated GIF and mp4 rotating around an OpenSCAD object.

set -e
d=$(basename `pwd`)
FRAMES=45
DIST=100

Xvfb :1 -screen 0 800x600x24 &
export DISPLAY=:1
for F in $(seq 1 $FRAMES); do
    X=`echo "$DIST*c(6.28318/$FRAMES*$F)" | bc -l`
    Y=`echo "$DIST*s(6.28318/$FRAMES*$F)" | bc -l`
    ZF=$(printf "%03d\n" $F)
    openscad -o $d-$ZF.png --camera=$X,$Y,$DIST,0,0,0 $d.scad 2>$d.log
done
pkill Xvfb

ffmpeg -y\
       -framerate 15 -pattern_type glob -i '*-*.png'\
       -f lavfi -i anullsrc\
       -r 15 -loop 0 "${d%/}.gif"\
       -r 15 -loop 0 -c:v libx264 -c:a aac -crf 0 -shortest "${d%/}.mp4"
tar -czf ${d%/}.tar.gz *.png && rm *.png
