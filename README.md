raven-xively
==========

A library to connect a Rainforest Automation RAVEn Smart Meter interface to a xively.com feed.

This is a fork of the excellent raven-cosm code, with small updates to get it working
with Xively. Pachube became cosm which became xively, yeesh.

Documentation in on the way.

Requirements
============

In addtion to the Requests library, you also need the [xively-python](https://github.com/xively/xively-python)
library. I didn't find it on PyPi, so you probably need to clone it from source and
run

  python setup.py install

from the checkout.

Installation and running
========================

You need the device driver for the Raven, and also have to edit the Info.plist
as Rainforest chose to use their own USB IDs. See [this thread for details](http://forums.whirlpool.net.au/archive/1928671).

* Setup your feed and channel on Xively. You'll need the feed ID (a number),
the channel name, and the API key (long hex string)
* Setup the API key in your shell, I reused the existing code for now so it's

  export COSM_API_KEY=longhexstring

* Modify lib/xively_writer.py - the feed ID and channel name

To run it

  cd lib
  python xively_logger.py

Debugging
=========

There's a commented line in xively_logger.py where you can add in the Echo
class; this is nice as it shows the raw XML from the Raven.

Notes and limitations
=====================

The Raven also outputs the total usage every now and then, this code skips that. Should
be easy to add, as the codebase is really quite elegant.
