import press_key as pk
import subprocess as sp
from setting import setting_menu_loop
from clean import clear_screen
from manage_openclaw import *
import json

main_button_num=1
max_main_menu=9

main_text={}
def input_lang():
    global main_text
    lang_file=r''
    with open(r"lang\lang_setting.json",'r',encoding='utf-8') as t:
        lang_file=json.load(t)["lang_file"]
    with open(lang_file,'r',encoding='utf-8') as t:
        main_text=json.load(t)["main"]
input_lang()

def main_menu():
    choose_button={'y':"> ",'n':"  "}

    #-------menu-------#
    print(main_text["title"])
    print("-----------------------")
    
    if(main_button_num==1): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(main_text["start"])

    if(main_button_num==2): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(main_text["start_with_port"])

    if(main_button_num==3): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(main_text["stop"])

    if(main_button_num==4): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(main_text["restart"])
    
    if(main_button_num==5): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(main_text["update"])

    if(main_button_num==6): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(main_text["fix"])

    if(main_button_num==7): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(main_text["uninstall"])

    if(main_button_num==8): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(main_text["install"])

    if(main_button_num==9): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(main_text["tool_box_setting"])

    print("-----------------------")

def main_menu_loop():
    global main_button_num

    clear_screen()
    main_menu()

    while True:
        flag=0
        key=pk.get_pressed_key()
        if(key=="UP"  ): 
            main_button_num-=1;flag=1
        if(key=="DOWN"): 
            main_button_num+=1;flag=1
        
        if(key=="ENTER"): 
            if(operation_main_menu()==1):
                break
            continue

        if(main_button_num>max_main_menu): 
            main_button_num=max_main_menu;flag=0
        if(main_button_num<1): 
            main_button_num=1;flag=0
        
        if(flag):
            clear_screen()
            main_menu()  

def operation_main_menu():
    clear_screen()

    #优先判断

    if(main_button_num==9):
        setting_menu_loop()
        input_lang()
        clear_screen()
        main_menu()
        return 0

    #控制台
    print(main_text["console"])
    print("-----------------------\n")

    if(main_button_num==1):
        sp.call("openclaw gateway start", shell=True)
        sp.call("openclaw dashboard", shell=True)
    if(main_button_num==2):
        port=input("输入端口: ")
        sp.call("openclaw gateway --port "+port, shell=True)
        sp.call("openclaw dashboard", shell=True)
    if(main_button_num==3):
        sp.call("openclaw gateway stop", shell=True)
    if(main_button_num==4):
        sp.call("openclaw gateway restart", shell=True)
    if(main_button_num==5):
        sp.call("openclaw update", shell=True)
    if(main_button_num==6):
        sp.call("openclaw doctor --fix", shell=True)
    if(main_button_num==7):
        uninstall_openclaw()
    if(main_button_num==8):
        install_openclaw()

    print("\n"*2+"-----------------------")
    print(main_text["back_main_menu"])
    while(pk.get_pressed_key()!='b'): pass

    clear_screen()
    main_menu()

main_menu_loop()