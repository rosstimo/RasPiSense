#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class RFID:

    def read():
        reader = SimpleMFRC522()
        try:
            id, text = reader.read()
        finally:
            GPIO.cleanup()
        return {"tagID":id, "text":text}

if __name__ == '__main__' :
    print(RFID.read()["tagID"])
    print(RFID.read()["text"])
