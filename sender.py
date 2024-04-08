# LED Control – Sender Side Code
import socket
import RPi.GPIO as GPIO
from gpiozero import LED
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(LED_PIN, GPIO.OUT)
LED_PIN = 7
led_red = LED(LED_PIN)
    
# Sender IP and port
target_ip = "localhost" # Replace with the IP of the connecting device
target_port = 7001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, target_port))
print("Connected to receiver")
 
try:
    while True:
        command = input("Enter 'on' to turn LED on, 'off' to turn LED off:")
        s.send(command.encode())
        response = s.recv(1024).decode()
        print(response)
        if response == "on":
            led_red.blink(0.1, 0.2, 5)
            print("The remote led has been turned on")
        elif response == "off":
            led_red.blink(0.1, 0.5, 5)
            print("The remote led has been turned off")
        else:
            led_red.blink(0.5, 1, 2)
            print("Command is invalid!")
 
except KeyboardInterrupt:
    print("\nExisting...")
    GPIO.cleanup()
    s.close()
finally:
    GPIO.cleanup()
    s.close()

