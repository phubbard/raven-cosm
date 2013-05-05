from subject import *
from observer import *
import threading
import serial

class USBIO(Subject, Observer):
    """subject / observer interface for a serial USB device: Any
    message received via update() is written to the USB device
    directly.  Any data read from the USB device is broadcast to
    observers.  Note that reads from the USB device happen in a
    separate thread.
    """

    def __init__(self, port="/dev/ttyUSB0", baud=115200):
        Subject.__init__(self)
        Observer.__init__(self)
        self.serial = serial.Serial(port, baud)
        self.thread = None

    # support for observer

    def update(self, subject, message):
        self.serial.write(message)

    # support for threading

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.thread = None

    # this code runs in a separate thread.
    def run(self):
        while threading.current_thread() == self.thread:
            line = self.serial.readline()
            self.notify(line)
            

