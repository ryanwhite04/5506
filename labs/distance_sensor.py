
from RPi.GPIO import setmode, setup, output, input, cleanup, BOARD, OUT, IN, LOW, HIGH
from time import sleep, time
from gpiozero import DistanceSensor


SOUND_SPEED = 343 # m/s

def main(trigger, echo):
    try:
        setmode(BOARD)
        setup(trigger, OUT)
        setup(echo, IN)
        output(trigger, LOW)
        print("Waiting for sensor to settle")
        sleep(2)
        print("Calculating distance")
        output(trigger, HIGH)
        sleep(0.00001)
        output(trigger, LOW)
        while not input(echo) :
            pulse_start_time = time()
        while input(echo):
            pulse_end_time = time()
        
        duration = pulse_end_time - pulse_start_time
        distance = duration * SOUND_SPEED / 2
        print(f"Distance: {distance * 100:.0f}cm")
    finally: cleanup()

def main2(trigger, echo):
    sensor = DistanceSensor(echo=echo, trigger=trigger)
    try:
        print("Waiting for sensor to settle")
        sleep(2)  # Wait for the sensor to settle
        print("Calculating distance")
        distance = sensor.distance * 100  # Convert to cm
        print(f"Distance: {distance:.0f}cm")
    except KeyboardInterrupt:
        print("Measurement stopped by user")
        
if __name__ == "__main__": main(7, 11)