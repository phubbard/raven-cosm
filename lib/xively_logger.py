import usbio
import echo
import xml_tag_extractor
import datapoint_extractor
import xively_writer

usb = usbio.USBIO()
idx = xml_tag_extractor.XMLTagExtractor("InstantaneousDemand")
dpx = datapoint_extractor.DatapointExtractor()
cos = xively_writer.XivelyWriter()
ech = echo.Echo()

# usb.attach(idx).attach(dpx).attach(cos).attach(ech)
usb.attach(idx).attach(dpx).attach(cos)
usb.start()
usb.thread.join()
