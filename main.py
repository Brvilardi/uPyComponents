from machine import Pin

from seven_segments_display import SevenSegmentsDisplay

a = Pin(17, Pin.OUT)
b = Pin(16, Pin.OUT)
c = Pin(14, Pin.OUT)
d = Pin(13, Pin.OUT)
e = Pin(12, Pin.OUT)
f = Pin(18, Pin.OUT)
g = Pin(19, Pin.OUT)
dp = Pin(15, Pin.OUT)

comp = SevenSegmentsDisplay(a, b, c, d, e, f, g, dp, common_anode=False)


