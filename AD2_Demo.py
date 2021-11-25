from AD2_functions import *
from threading import *

gen1 = Thread(target=GenSet, args=(3e6, 1, False),)
gen2 = Thread(target=GenSet, args=(3e6, 2, False),)
gen3 = Thread(target=GenSet, args=(3e6, 3, False),)

gen1.start()
time.sleep(1)
for i in range(5):
    P2P = GetP2P(2000, False)
    print(P2P + "\n")
gen1.join()

gen2.start()
time.sleep(1)
for i in range(5):
    P2P = GetP2P(2000, False)
    print(P2P + "\n")
gen2.join()

gen3.start()
time.sleep(1)
for i in range(5):
    P2P = GetP2P(2000, False)
    print(P2P + "\n")
gen3.join()



# GenSet(3e6,1,False)
# GetP2P(2000,False)





