import os, ctypes, sys
from time import sleep

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def clear():
    os.system("cls")

if is_admin():
    # Kill main .exe's
    clear()
    print("Killing Wacom_Tablet.exe...")
    os.system("taskkill /F /IM Wacom_Tablet.exe")

    clear()
    print("Killing Pen_Tablet.exe...")
    os.system("taskkill /F /IM Pen_Tablet.exe")

    # Kill main services
    clear()
    print("Disabling WTabletService services...")
    os.system("net stop WTabletServicePro")
    os.system("net stop WTabletServiceCon")

    # Summary screen
    clear()
    print("Successfully disabled Wacom drivers.")
    print("\nExiting in 3 seconds...")
    sleep(3)
    exit()

else:
    # Restart with UAC
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)