import subprocess as sp
import json

main_text={}
def input_lang():
    global main_text
    lang_file=r''
    with open(r"lang\lang_setting.json",'r',encoding='utf-8') as t:
        lang_file=json.load(t)["lang_file"]
    with open(lang_file,'r',encoding='utf-8') as t:
        main_text=json.load(t)["main"]
input_lang()

def uninstall_openclaw():
    ask=input(main_text["chose"])
    while(not (ask=="y" or ask=="n")):
        ask=input(main_text["chose"])
        print('\033[H\033[2J', end='', flush=True)
    if(ask=='y'):
        sp.call("openclaw uninstall", shell=True)
        sp.call("npm uninstall -g openclaw",shell=True)

def install_openclaw():
    import sys
    if(sys.platform=='win32'):
        print(main_text["install_win"])
        sp.call('start powershell "iwr -useb https://openclaw.ai/install.ps1 | iex"',shell=True)
    else:
        sp.call("curl -fsSL https://openclaw.ai/install.sh | bash",shell=True)