class Subject:

    def __init__(self):
        self.observers = set()

    def notify(self, message):
        for observer in self.observers:
            try:
                observer.lock.acquire()
                observer.update(self, message)
            finally:
                observer.lock.release()

    def attach(self, observer):
        self.observers.add(observer)
        return observer         # facilitate chaining

    def detach(self, observer):
        self.observers.discard(observer)

