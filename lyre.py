import ctypes, sys
import keyboard, pyautogui, time
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_admin():
    # Code of your program here
    while True:
        if keyboard.is_pressed('q')==True :
            pyautogui.write('  Y  Y Y Y  T  R  E  R  w  e  r  t  y   t',interval=0.2)
            pyautogui.write('  Y  Y Y Y  T  R  E  R  w  e  r  e  r',interval=0.2)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    while True:
        if keyboard.is_pressed('q')==True :
            pyautogui.write('  Y  Y Y Y  T  R  E  R  w  e  r  t  y   t',interval=0.2)
            pyautogui.write('  Y  Y Y Y  T  R  E  R  w  e  r  e  r',interval=0.2)
    
