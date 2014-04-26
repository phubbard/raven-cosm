from subject import *
from observer import *
import os
import sys
import xively

class XivelyWriter(Subject, Observer):

    def __init__(self):
        Subject.__init__(self)
        Observer.__init__(self)
        self.api = xively.XivelyAPIClient(self.api_key())
        self.feed = self.api.feeds.get(self.FEED_ID)
        self.datastream = self.feed.datastreams.get('PowerMeter')

    API_PREFIX = 'https://api.xively.com/v2'
    FEED_ID='571033480'

    # support for observer

    def update(self, subject, message):
      self.datastream.current_value = message['value']
      self.datastream.at = message['at']
      self.datastream.update()
      self.notify(message)
      print(message['value'] + ' ' + message['at'])

    def api_key(self):
        return os.environ["COSM_API_KEY"]
