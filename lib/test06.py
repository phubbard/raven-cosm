import usbio
import echo
import xml_tag_extractor
import datapoint_extractor

usb = usbio.USBIO()
idx = xml_tag_extractor.XMLTagExtractor("InstantaneousDemand")
dpx = datapoint_extractor.DatapointExtractor()
ech = echo.Echo()

usb.attach(idx).attach(dpx).attach(ech)
# usb.attach(idx).attach(ech)
usb.start()
usb.thread.join()

