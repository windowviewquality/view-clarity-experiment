#Contrast Sensitivity Test - V.0.1
"""
This is a python code that displays Contrast Sensitivity test on a computer monitor. 
Users will need to calibrate the display size and color 
according to their monitor screen.
"""
#Copyright (c) 2023, Dong Huk (Seth) Park, Stealth Startup

#__author__ = "Dong Huk Park"
#__date__ = "2023.07.24"
#__version__ = "V.0.1"

import numpy as np
import psychopy
from psychopy.visual import Window, TextStim

win = Window(pos=[50, 50], color=(1.0, 1.0, 1.0), size=(1400, 1000))
i = 0
values = [0.0, 0.29, 0.5, 0.65, 0.74, 0.81, 0.87, 0.9, 0.93, 0.95, 0.96, 0.98]
alphabets = ['V', 'R', 'S', 'K', 'D', 'R', 'N', 'H', 'C', 'O', 'Z']
cache = set()
while True:
    v = values[i]
    print('current value', v)

    while True:
        alpha = np.random.choice(alphabets)
        if alpha not in cache:
            cache.add(alpha)
            break
    stim = TextStim(win, '%s' % alpha, height=0.4, bold=True,
                    pos=(0.0, 0.0), font= 'Optician Sans', color=(29, 1e-9, v), colorSpace='hsv')
    stim.draw()
    win.flip()
    kill_session = False

    while True:
        toggle = input("Possible options: n, j")
        if toggle  == 'j':
            i += 1
            cache = set()
            break
        elif toggle == 'n':
            break
        elif toggle == 'exit':
            kill_session = True
            break
        else:
            print("Invalid key")
   
    if kill_session:
        break
win.close()
