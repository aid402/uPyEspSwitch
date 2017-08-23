from machine import Pin

class Config:
        
    def __init__(self, box_id, pinButton, pinSwitch, patternList):
        self.state = 0
        self.box_id = box_id
        self.Button = Pin(pinButton, Pin.IN, Pin.PULL_UP)
        self.
        self.patternList = patternList
        
        
        for i in range(len(pinRelay)):
            self.relay[i] = Pin(pinRelay[i], Pin.OUT, value=0)
        
    def turn(self, pattern_num):
        p = self.Pattern[pattern_num]
        for n in range(len(self.relay)):
            self.relay[n].value(int(p[n]))
    
    def push(self):
        self.state += 1
        if self.state >= len(self.relay) :
            self.state = 0
        return self.state
