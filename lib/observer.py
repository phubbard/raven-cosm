import threading

class Observer:

    def __init__(self):
        self.lock = threading.RLock()

    def update(self, subject, message):
        raise NotImplementedError("must subclass me")


