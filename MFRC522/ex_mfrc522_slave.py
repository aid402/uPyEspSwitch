from machine import Pin, SPI
from mfrc522 import MFRC522_slave

spi = SPI(-1,baudrate=100000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
rst = Pin(0,Pin.OUT)
cs1 = Pin(15,Pin.OUT)
cs2 = Pin(5,Pin.OUT)
cs3 = Pin(4,Pin.OUT)

rdr1 = MFRC522_slave(spi,rst,cs1)
rdr2 = MFRC522_slave(spi,rst,cs2)
rdr3 = MFRC522_slave(spi,rst,cs3)
