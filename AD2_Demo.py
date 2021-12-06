from AD2_BCC import *

Device = AD2()

Device.GenSet(3e6, 1, 0)
P2P_1 = Device.GetP2P (8192, 0)

Device.GenSet(3e6, 2.5, 0)
P2P_2 = Device.GetP2P (8192, 0)

Device.GenSet(3e6, 5, 0)
P2P_3 = Device.GetP2P (8192, 0)

print(P2P_1, P2P_2, P2P_3)

Device.close()
