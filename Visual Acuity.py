#Visual Acuity Test - V.0.1
"""
This is a python code that displays Visual Acuity test on a computer monitor. 
Users will need to calibrate the display size and color 
according to their monitor screen.
"""
#Copyright (c) 2023, Dong Huk (Seth) Park, Stealth Startup

#__author__ = "Dong Huk Park"
#__date__ = "2023.07.24"
#__version__ = "V.0.1"

import numpy as np
from psychopy.visual import Window, TextStim

win = Window(color=(1.0, 1.0, 1.0))
i = 0
distances = [400, 320, 250, 200, 100, 70, 60, 50, 40, 30, 20, 15, 10, 7, 4]
alphabets = ['C', 'D', 'E', 'F', 'L', 'N', 'O', 'P', 'T', 'Z']
cache = set()

while True:
    d = distances[i]
    print('current distance', d)
    while True:
        alpha = np.random.choice(alphabets)
        if alpha not in cache:
            cache.add(alpha)
            break
    factor = 0.0032
    fontsize = d * factor
    stim = TextStim(win, '%s' % alpha, height=fontsize, bold=True,
                    pos=(0.0, 0.0), font = 'Optician Sans',
                    color=(29, 1e-9, 1e-9), colorSpace='hsv')
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
