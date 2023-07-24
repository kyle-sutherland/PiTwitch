import time
import OPiRgbLed
from OPiRgbLed import control as rgbled


def alertPurple(flash = 2, ontime = 0.2, offtime = 0.1):
    i = 0
    while i < flash:
        rgbled.purple()
        time.sleep(ontime)
        rgbled.off()
        time.sleep(offtime)
        i += 1


def alertPurpleYellow(flash = 3, ytime = 0.2, ptime = 0.2):
    i = 0
    while i < flash:
        rgbled.purple()
        time.sleep(ptime)
        rgbled.yellow()
        time.sleep(ytime)
        i += 1
