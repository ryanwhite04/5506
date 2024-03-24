
ffmpeg -framerate 10 -i %03d.jpg -c:v libx264 -pix_fmt yuv420p stop_motion.mp4
