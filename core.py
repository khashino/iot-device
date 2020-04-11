import ui
import finger
import status
import threading
import time
import indicators

for i in range(10):
    indicators.blinkall(0.1)
    time.sleep(1)

counter = 0
while True:
    if counter % 15 == 0:
        thread1 = threading.Thread(target=status.checker()).start()
    if counter % 2 == 0:
        #time.sleep(1)
        f=finger.fingerinit()
        if f.readImage() == True:
            finger.fingerop(f)
    thread2 = threading.Thread(target=ui.clockmain()).start()
    time.sleep(0.5)
    counter += 1
    if counter == 1000:
        counter = 0
