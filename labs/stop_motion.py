from picamera import PiCamera
from gpiozero import Button

button = Button(2)

def main():
    camera = PiCamera()
    camera.resolution = (640, 480)
    frame = 0
    print("Press button to capture")
    while True:
        button.wait_for_press()
        # frames are of name 01.jpg and so on, so count has to be left padded
        camera.capture(f'frames/{str(frame).zfill(2)}.jpg')
        frame += 1
        if frame == 20:
            break
    camera.close()