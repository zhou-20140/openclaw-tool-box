def clear_screen():
    import sys
    import os
    os = sys.platform
    if os == "win32":
        import os
        os.system('cls')
    if os == "linux" or os == "darwin":
        import os
        os.system('clear')
    else:
        print("\033c",flush=True)