import press_key as pk
import json

setting_button_num=1
max_setting_menu=4

about=[]
def input_lang():
    global about
    global setting_text
    lang_file=r''
    with open(r"lang\lang_setting.json",'r',encoding='utf-8') as t:
        lang_file=json.load(t)["lang_file"]
    with open(lang_file,'r',encoding='utf-8') as t:
        setting_text=json.load(t)["setting"]
    about=setting_text["about_context"]
input_lang()

from language import language_menu_loop

def setting_menu_loop():
    global setting_button_num

    print('\033[H\033[2J', end='', flush=True)
    setting_menu()

    input_lang()

    while True:
        input_lang()
        
        flag=0
        key=pk.get_pressed_key()
        if(key=="UP"  ): 
            setting_button_num-=1;flag=1
        if(key=="DOWN"): 
            setting_button_num+=1;flag=1
        
        if(key=="ENTER"): 
            if(operation_setting_menu()==1):
                break
            continue
        
        if(setting_button_num>max_setting_menu): 
            setting_button_num=max_setting_menu;flag=0
        if(setting_button_num<1): 
            setting_button_num=1;flag=0
        

        
        if(flag):
            print('\033[H\033[2J', end='', flush=True)
            setting_menu()

def operation_setting_menu():

    if(setting_button_num==1):
        return 1
    
    if(setting_button_num==2):
        print('\033[H\033[2J', end='', flush=True)
        for i in about:
            print(i)
        print(setting_text["back_setting_menu"])
        while(pk.get_pressed_key()!='b'): pass
        print('\033[H\033[2J', end='', flush=True)
        setting_menu()

    if(setting_button_num==3):
        language_menu_loop()
        print('\033[H\033[2J', end='', flush=True)
        input_lang()
        setting_menu()
        return 0

    if(setting_button_num==4):
        print('\033[H\033[2J', end='', flush=True)
        exit()

    return 0


def setting_menu():
    print('\033[H\033[2J', end='', flush=True)
    choose_button={'y':"> ",'n':"  "}

    #-------menu-------#
    print(setting_text["title"])
    print("-----------------------")

    if(setting_button_num==1): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(setting_text["back"])

    if(setting_button_num==2): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(setting_text["about"])

    if(setting_button_num==3): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(setting_text["language"])

    if(setting_button_num==4): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print(setting_text["exit"])

    print("-----------------------")