from re import A
from AD2_BCC import *

Amplitude = 1 
FRQ = [5e4, 1e5, 2e5, 3e5, 4e5, 5e5, 6e5, 7e5, 8e5, 9e5, 1e6, 1.5e6, 2e6, 2.5e6, 3e6, 3.5e6, 4e6, 4.5e6, 5e6, 1e7, 1.5e7, 2e7, 2.5e7]
GenChannel = 0
ScopeChannel = 0
BufferSize = 8000
Buffer = []

Device = AD2()



# print(min(Device.GetScopeData(1000,ScopeChannel))*1000)

for i in range(len(FRQ)):
    # Device.setupGenerator(FRQ[i], Amplitude, GenChannel)
    input('')
    Buffer.append(Device.getScopeBuffer(8000, ScopeChannel))
    print('Frequency is ' + str(FRQ[i]) + ' Hz')


    print(Device.getPeakToPeak(8000, ScopeChannel))


Device.close()
# print(Buffer)

File = open('Transmitter_AD2scope_TektronixGenerator.csv', 'w')
for j in range(len(FRQ)):
    File.writelines(str(Buffer[j]) + "\n")

File.close()
