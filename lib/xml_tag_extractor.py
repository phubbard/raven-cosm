from subject import *
from observer import *
import re

class XMLTagExtractor(Subject, Observer):
    """Receives XML strings via update() method.  Searches for
    a specific <tag_name> in the XML stream and collects all
    XML upto and including the corresponding </tag_name> before
    emitting it to observers via notify().
    """

    def __init__(self, tag_name):
        Subject.__init__(self)
        Observer.__init__(self)
        self.tag_name = tag_name
        self.re_open = re.compile('.*?(<' + self.tag_name + '>)(.*)', flags=re.DOTALL)
        self.re_clos = re.compile('(.*<\/' + self.tag_name + '>)(.*)', flags=re.DOTALL)
        self.state = 0
        self.xml_input = ""
        self.collected_fragment = ""

    # support for observer

    def update(self, subject, message):
        self.process_input(message)

    # ================================================================

    # NB: doesn't handle nested:
    # <tag_name> ... 
    #   <tag_name> ... </tag_name>
    # </tag_name>
    def process_input(self, string):
        self.xml_input += string

        while True:
            if (self.state == 0):
                # searching for <tag_name>...
                m = self.re_open.search(self.xml_input)
                if not(m): return
                # here: m.group(1) is <tag_name>, m.group(2) is anything
                # following it
                self.collected_fragment = m.group(1)
                self.xml_input = m.group(2)
                self.state = 1
                # fall through...
                
            m = self.re_clos.search(self.xml_input)
            # searching for </tag_name>...
            if not(m): return
            # here: m.group(1) is everything upto and including </tag_name>,
            # m.group(2) is anything following it.
            self.collected_fragment += m.group(1)
            self.xml_input = m.group(2)
            self.state = 0
            self.notify(self.collected_fragment)

