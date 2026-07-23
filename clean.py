import sys
import subprocess as sp
def clear_screen():
    if sys.platform == "win32":
        sp.run(['cls'], shell=True)
    if sys.platform == "linux" or sys.platform == "darwin":
        sp.run(['clear'], shell=True)
    else:
        print("\033c",flush=True)