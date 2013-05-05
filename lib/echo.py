from subject import *
from observer import *

class Echo(Subject, Observer):

    def __init__(self):
        Subject.__init__(self)
        Observer.__init__(self)

    # support for observer

    def update(self, subject, message):
        print message,
        self.notify(message)



