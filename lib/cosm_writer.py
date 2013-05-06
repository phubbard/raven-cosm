from subject import *
from observer import *
import requests
import json

class CosmWriter(Subject, Observer):

    def __init__(self):
        Subject.__init__(self)
        Observer.__init__(self)

    API_PREFIX='http://api.cosm.com/v2'
    FEED_ID='129722'

    # support for observer

    def update(self, subject, message):
        r = requests.post(API_PREFIX + '/feeds/' + FEED_ID + '/datastreams/1/datapoints',
                          data=json.dumps(message),
                          headers = {'X-ApiKey': self.cosm_api_key()})
        if r.status_code >= 300:
            sys.stderr.write(r.content + "\n")
        self.notify(message)

    def cosm_api_key(self):
        return os.environ["COSM_API_KEY"]
