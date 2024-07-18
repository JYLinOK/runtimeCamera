# Main code of the RuntimeCamera
# Jinwei Lin 
# July 18, 2024
# 林进威
# 2024年7月18日

import time
import sys

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
with open('./icon/icon.txt', 'r') as F:  
    icon = F.read()  
    # print(icon)
delayPrint(icon)
# delayPrintLine(icon, 0.001)
print(line)
print(line)

Ta = 0.03
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


