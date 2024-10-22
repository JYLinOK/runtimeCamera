# Main code of the RuntimeCamera
# Jinwei Lin 
# July 18, 2024
# 林进威
# 2024年7月18日

import time
import sys
import os
import platform
import keyboard

# =========================================================================















# =========================================================================

def delayPrint(S, t=0.02):
    S_L = S.split('\n')
    for s_it in S_L:
        print(s_it)
        # print('\n')
        time.sleep(t)


def delayPrintLine(L, t=0.05):
    for i in L:
        print(i, end=''),
        sys.stdout.flush()
        time.sleep(t)


def detectSystem():
    system = ''
    if sys.platform.startswith('linux'):
        system = 'linux'
    elif sys.platform.startswith('win'):
        system = 'windows'
    elif sys.platform.startswith('darwin'):
        system = 'macOS'
    else:
        system = 'other'
    return system



line = '===================================================================================================='
print(line)
print(line)
with open('./icon/jinwei.txt', 'r') as F:  
    icon = F.read()  
    # print(icon)
delayPrint(icon)
# delayPrintLine(icon, 0.001)
print(line)
print(line)

# For Linux hardware event id
keyboardEventID = 3

# with open('./icon/icon2.txt', 'r') as F:  
#     icon2 = F.read()  
#     # print(icon)
# delayPrint(icon2)

print()
delayPrintLine('==== RuntimeCamera ===', 0.01)
print()

Ta = 0.02
delayPrintLine('Please Selete the functions:', Ta)
print()
delayPrintLine('Press key 1 => run rc1_only_camera.py', Ta)
print()
delayPrintLine('Press key 2 => run rc2_face_camera.py', Ta)
print()
delayPrintLine('Press key 3 => run rc3_face_body_camera.py', Ta)
print()
delayPrintLine('Press key e => exit', Ta)
print()
delayPrintLine(line, 0.01)
print()


def on_key(event):
    if event.name not in ['1', '2', '3', 'e', 'q']:
        print('You pressed ' + event.name + 'key')
    else:
        if event.name == '1':
            os.system('python rc1_only_camera.py')
        elif event.name == '2':
            os.system('python rc2_face_camera.py')
        elif event.name == '3':
            os.system('python rc3_face_body_camera.py')
        elif event.name == 'q':
            sys.exit('exit')


def on_key_linux():
    id_key = input()
    if id_key not in ['1', '2', '3', 'e', 'q']:
        print('You pressed ' + id_key + 'key')
    else:
        if id_key == '1':
            os.system('python rc1_only_camera.py')
        elif id_key == '2':
            os.system('python rc2_face_camera.py')
        elif id_key == '3':
            os.system('python rc3_face_body_camera.py')
        elif id_key == 'q':
            sys.exit('exit')
        else:
            print('Please select again')
        on_key_linux()


def Runtime():
    system = detectSystem()
    print(f'{system = }')

    
    if system == 'windows':
            keyboard.on_press(on_key)
            keyboard.wait()
    else:
        on_key_linux()

Runtime()

