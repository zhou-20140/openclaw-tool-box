import press_key as pk
import json
import os

language_button_num=1
max_language_menu=2

def operation_language_menu():
    lang_file=r''
    if(language_button_num==1):
        lang="en_US"
    if(language_button_num==2):
        lang="zh_CN"
    lang_file=os.path.join(r"lang",lang+'.json')
    with open(r"lang\lang_setting.json",'w') as t:
        data={
            "lang":lang,
            "lang_file":lang_file
        }
        json.dump(data,t)
    return 1

def language_menu_loop():
    global language_button_num

    print('\033[H\033[2J', end='', flush=True)
    language_menu()

    while True:
        flag=0
        key=pk.get_pressed_key()
        if(key=="UP"  ): 
            language_button_num-=1;flag=1
        if(key=="DOWN"): 
            language_button_num+=1;flag=1
        
        if(key=="ENTER"): 
            if(operation_language_menu()==1):
                break
            continue
        
        if(language_button_num>max_language_menu): 
            language_button_num=max_language_menu;flag=0
        if(language_button_num<1): 
            language_button_num=1;flag=0
        

        
        if(flag):
            print('\033[H\033[2J', end='', flush=True)
            language_menu()

def language_menu():
    print('\033[H\033[2J', end='', flush=True)
    choose_button={'y':"> ",'n':"  "}

    if(language_button_num==1): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print("English")

    if(language_button_num==2): print(choose_button['y'],end='')
    else: print(choose_button['n'],end='')
    print("简体中文")
    