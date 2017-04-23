ffmpeg  -f lavfi -i aevalsrc="sin(440*3*PI*t)|cos(440*PI*t):s=8000" \
    -f wav -
