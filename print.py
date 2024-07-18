import sys
from time import sleep

def slow(text):
    for i in text:
        print(i, end=''),
        sys.stdout.flush()
        sleep(0.2)
    # return '.'.endswith('')

slow('loginning')