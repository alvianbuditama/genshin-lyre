import keyboard
from pyautogui import press as pypress
from pyautogui import write as pywrite

def trust_in_you():
    a=0.1
    # pywrite(" d    d d d f g f d s ",interval=a);
    # pywrite(' d d d  f g  f d   s   s   d   n    g   h   d ',interval=a)
    # pywrite(' n  n  n  m  a s a m ',interval=a)
    # pywrite(' d    d d  d f g  f d s ',interval=a)
    pywrite(' d d d  f  g  q  j  g  s  d     g   h   d',interval=a)








try:
 while True:
    if keyboard.is_pressed('1'):
        trust_in_you()


except KeyboardInterrupt:
    print("Interrupted")
