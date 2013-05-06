from subject import *
from observer import *
import sys

class Echo(Subject, Observer):

    def __init__(self):
        Subject.__init__(self)
        Observer.__init__(self)

    # support for observer

    def update(self, subject, message):
        print message,
        sys.stdout.flush()
        self.notify(message)



