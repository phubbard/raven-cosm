from subject import *
from observer import *
import requests
import json
import os
import sys

class CosmWriter(Subject, Observer):

    def __init__(self):
        Subject.__init__(self)
        Observer.__init__(self)

    #API_PREFIX='http://api.cosm.com/v2'
    API_PREFIX = 'https://api.xively.com/v2'
    FEED_ID='571033480'

    # support for observer

    def update(self, subject, message):
        body = {"datapoints":[message]}
        r = requests.post(self.API_PREFIX + '/feeds/' + self.FEED_ID + '/datastreams/1/datapoints.json',
                          data=json.dumps(body),
                          headers = {'X-ApiKey': self.cosm_api_key()})
        if r.status_code >= 300:
            sys.stderr.write("Error:" + r.content + "\n")
        self.notify(message)

    def cosm_api_key(self):
        return os.environ["COSM_API_KEY"]
