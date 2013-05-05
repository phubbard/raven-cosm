from subject import *
import threading
import time

class FileReader(Subject):

    def __init__(self, filename):
        Subject.__init__(self)
        self.filename = filename
        self.thread = None

    # support for threading

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.thread = None

    # this code runs in a separate thread.
    def run(self):
        file = open(self.filename)
        try:
            while threading.current_thread() == self.thread:
                line = file.readline()
                if not(line): break
                self.notify(line)
                time.sleep(0.25)
        finally:
            file.close()


