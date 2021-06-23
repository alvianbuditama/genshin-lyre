import keyboard
from pyautogui import press as pypress
from pyautogui import write as pywrite


a=0.09
b=a*2;c=a*3;aa=0;q=a*6;w=a*5
try:
 while True:
    if keyboard.is_pressed('1')==True :
        pypress(['c','q'],interval=a);pywrite('w t q w t',interval=a);pypress(['d','q'],interval=a);pywrite('w t q w t',interval=a)
        pypress(['v','q'],interval=a);pywrite('w t q w t',interval=a);pypress(['f','q'],interval=a);pywrite('w t q w t',interval=a)
        pypress(['n','q'],interval=a);pywrite('w t q w t',interval=a);pypress(['h','q'],interval=a);pywrite('w t',interval=a);pypress(['b','q'],interval=a);pywrite('w t',interval=a)
        pypress(['c','q'],interval=a);pywrite('w t q w t',interval=a);pypress(['d','q'],interval=a);pywrite('w t q w t',interval=a)
        pypress(['d','q'],interval=a);pywrite('w t q w t',interval=a);pypress(['v','q'],interval=a);pywrite('w t q w t',interval=a)
        pypress(['f','q'],interval=a);pywrite('w t q w t',interval=a);pypress(['b','q'],interval=a);pywrite('w t q w t',interval=a)
        pypress(['g','q'],interval=a);pywrite('w t q w t q w t',interval=a);pypress(['z','q'],interval=a);pywrite('w t',interval=a)
        pypress(['b','q'],interval=a);pywrite('w t',interval=a);pypress(['a','q'],interval=a);pywrite('w t',interval=a);pypress('c',interval=c);pywrite('e e e',interval=a)
        pypress(['d','e'],interval=a);pywrite('w w  q',interval=a);pypress(['v','q'],interval=q);pywrite('f      b   e e e',interval=a);
        pypress(['g','e'],interval=b);pywrite('w w  q',interval=a);pypress(['n','e'],interval=a);pywrite('e  t',interval=a);pypress(['h','w'],interval=c)
        pypress(['b','q'],interval=c);pywrite('c   e e e',interval=a);pypress(['d','e'],interval=b);pywrite('w w  q',interval=a);
        pypress(['v','q'],interval=q);pywrite('f     b   e e e',interval=a);pypress(['g','e'],interval=b);pywrite('w w  q q   z   b   a   c   e e e',interval=a)
        pypress(['d','e'],interval=b);pywrite('r e  w',interval=a);pypress(['v','q'],interval=q);pywrite('f      b   e e e',interval=a)
        pypress(['g','e'],interval=b);pywrite('w w  q',interval=a);pypress(['n','e'],interval=c);pywrite('e  t',interval=a)
        pypress(['h','w'],interval=c);pypress(['b','q'],interval=c);pywrite('c   e e e',interval=a);pypress(['d','e'],interval=b);pywrite('w w  q',interval=a)
        pypress(['v','q'],interval=c);pypress('q',interval=c);pypress(['f','q'],interval=c);pywrite('q   q   b   w w w',interval=a);pypress(['g','w'],interval=b);pywrite('e w  q',interval=a)
        pypress(['g','q'],interval=q);pypress('g',interval=q);pypress(['c','b','a'],interval=a);pywrite('s a   a',interval=a)
        pypress(['d','g','w'],interval=b);pypress(['g','q'],interval=b);pypress(['q','t'],interval=b);pypress(['v','q','r'],interval=w);pypress('a',interval=a)
        pypress(['f','g'],interval=a);pywrite('h q q w q',interval=a);pypress(['z','b','w'],interval=a);pywrite('e u e w u',interval=a)
        pypress(['a','e'],interval=a);pywrite('w y w q y',interval=a);pypress(['a','t'],interval=q);pypress('a',interval=q);pypress(['c','b','a'],interval=a);pywrite('s a   a',interval=a)
        pypress(['d','g','w'],interval=b);pypress(['g','q'],interval=b);pypress(['q','t'],interval=b);pypress(['v','q','r'],interval=w);pypress('a',interval=a)
        pypress(['f','g'],interval=a);pywrite('h q q w q',interval=a);pypress(['z','b','g','q'],interval=b);pypress(['g','w'],interval=c);pypress('b',interval=a)
        pypress(['a','q','r'],interval=a);pywrite('d a   b n b      ',interval=a);pypress(['q'],interval=0.015);pypress(['w'],interval=0.015);pypress('t',interval=q)
        pypress(['c','a'],interval=c);pywrite('e w w',interval=a);pypress(['d','w'],interval=a);pywrite('q q q  w',interval=a);pypress(['q','v','a'],interval=q);pypress('f',interval=q)
        pypress(['b','s'],interval=c);pywrite('e e e',interval=a);pypress(['g','e'],interval=b);pywrite('w w  q',interval=a);pypress(['n','d','e'],interval=c);pywrite('e  t',interval=a)
        pypress(['h','w'],interval=c);pypress(['b','q'],interval=c);pypress(['c','a'],interval=c);pywrite('e e e',interval=a);pypress(['d','e'],interval=b);pywrite('r e  w',interval=a)
        
        


except KeyboardInterrupt:
    print("Interrupted")