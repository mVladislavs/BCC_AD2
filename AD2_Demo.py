from AD2_functions import *
from threading import *

Device = AD2init()

gen1 = Thread(target=GenSet, args=(3e6, 1, False, Device[0]),)
gen2 = Thread(target=GenSet, args=(3e6, 2, False, Device[0]),)
gen3 = Thread(target=GenSet, args=(3e6, 5, False, Device[0]),)

gen1.start()
for i in range(5):
    P2P = GetP2P(8192, False, Device[1])
    print(P2P)
gen1.join()

gen2.start()
for i in range(5):
    P2P = GetP2P(8192, False, Device[1])
    print(P2P)
gen2.join()

gen3.start()
for i in range(5):
    P2P = GetP2P(8192, False, Device[1])
    print(P2P)
gen3.join()

AD2close(Device[0], Device[1])
