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
    # Start main services
    clear()
    print("Starting WTabletService services...")
    os.system("net start WTabletServicePro")
    os.system("net start WTabletServiceCon")

    # Summary screen
    clear()
    print("Successfully enabled Wacom drivers.")
    print("\nExiting in 3 seconds...")
    sleep(3)
    exit()

else:
    # Restart with UAC
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)