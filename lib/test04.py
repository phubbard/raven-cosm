import usbio
import echo

usb = usbio.USBIO()
usb.attach(echo.Echo())

usb.start()
usb.thread.join()

