sudo apt-get install adb ffmpeg    
adb exec-out screenrecord --output-format=h264 - |
   ffplay -framerate 60 -probesize 32 -sync video  -
