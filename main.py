from datetime import  datetime
from time import sleep
import sys

if __name__ == '__main__':
    pass

while True:
    print(datetime.now())
    sys.stdout.flush()
    sleep(30)
