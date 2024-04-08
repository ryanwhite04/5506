import socket
import RPi.GPIO as GPIO
from gpiozero import LED
LED_PIN = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Sender IP and port
target_ip = "0.0.0.0"
target_port = 7001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((target_ip, target_port))
s.listen(1)
print("Waiting for connection....")
conn, addr = s.accept()
print("Connected by", addr)
 
 
try:
    while True:
        command = conn.recv(1024).decode()

        if command == "on":
            GPIO.output(LED_PIN, GPIO.HIGH)
            res = "on"
            print("on")
        elif command == "off":
            GPIO.output(LED_PIN, GPIO.LOW)
            res = "off"
            print("off")
        else:
            res = "invalid"
            print("Invalid command")

            conn.send(res.encode())

except KeyboardInterrupt:
    print("\nExisting...")
    GPIO.cleanup()
    s.close()
finally:
    GPIO.cleanup()
    s.close()