ffmpeg -i http://streaming.witr.rit.edu:8000/witr-mp3-192 -af silenceremove=1:0:-50dB -ar 8000 -f wav -
