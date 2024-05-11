from tkinter import *
import random
import time

root = Tk()

rngdevice = Label(root)
rngdevice.pack()

def solsrng():
    funnynumber = random.randint(1, 1000)
    if funnynumber == (1):
        rngoutput = "you got the funnyest number"
    if funnynumber == (276):
        rngoutput = "wow good job you did an rng"
    if funnynumber == (215):
        rngoutput = "that's an oddly specific number"
    if funnynumber == (69):
        rngoutput = "you got the really cool aura!!!"
    if funnynumber == (1000):
        rngoutput = "you got 1000!"
    if 500 <= funnynumber <= 999:
        rngoutput = "you got the really common one"
    if 2 <= funnynumber <= 68:
        rngoutput = "this one is kinda rare!"
    if 68 <= funnynumber <= 214:
        rngoutput = "this one is not that common but still common"
    if 216 <= funnynumber <= 275:
        rngoutput = "really rare and specific but not 1 in 1000"
    if 277 <= funnynumber <= 419:
        rngoutput = "big majority of the numbers"
    if funnynumber == (420):
        rngoutput = "haha funny number"
    if 421 <= funnynumber <= 499:
        rngoutput = "im done with this"
    rngdevice.config(text=rngoutput)
    root.after(1000, solsrng)
    
solsrng()

root.mainloop()