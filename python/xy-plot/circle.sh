ffmpeg  -f lavfi -i aevalsrc="sin(440*2*PI*t)|cos(440*2*PI*t):s=8000" \
    -f wav -
