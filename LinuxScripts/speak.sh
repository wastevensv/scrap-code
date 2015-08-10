n=0
while read L; do
  espeak -v "english-us" -p 80 -a 200 -s 135 "$L" -w $n.wav
  n=$(($n+1))
done <lines.txt
