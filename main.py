# Main code of the RuntimeCamera
# Jinwei Lin 
# July 18, 2024
# 林进威
# 2024年7月18日

import time
import sys
import os

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


def Runtime():
    user_input = input() 
    # print(f'{user_input = }')

    if user_input == None:
        user_input = sys.stdin.read(1)

    if user_input not in ['1', '2', '3', 'e', 'q']:
        print('You pressed ' + user_input + 'key')
    else:
        if user_input == '1':
            os.system('python rc1_only_camera.py')
        elif user_input == '2':
            os.system('python rc2_face_camera.py')
        elif user_input == '3':
            os.system('python rc3_face_body_camera.py')
        elif user_input == 'q':
            sys.exit('exit')
        

Runtime()

