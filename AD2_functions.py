import dwf
import sys
import time

#######################################################################################
######################################################################################
#AD2init
#######################################################################################
######################################################################################


def AD2init():

    if len(dwf.DwfEnumeration()) == 0:
        sys.exit("No AD2 detected")

    hdwf = dwf.Dwf() # get token
    AO = dwf.DwfAnalogOut(hdwf) # open device as analog outpput 
    scope = dwf.DwfAnalogIn(hdwf) # open device as analog input 
    return AO, scope

#######################################################################################
######################################################################################
#AD2close
#######################################################################################
######################################################################################

def AD2close(AO, scope):

    scope.close() 
    AO.close()  

#######################################################################################
######################################################################################
#GenSet
#######################################################################################
######################################################################################

def GenSet(frequency:int, amplitude:float, channel:bool, AO):

    #Check input values
    if frequency > 5e7:
        sys.exit("Frequency cannot be > 50MHz")
    
    if frequency < 0:
        sys.exit("Frequency cannot be < 0Hz")
    
    if amplitude > 5:
        sys.exit("Amplitude cannot be > 5V")

    if amplitude < 0:
        sys.exit("Amplitude cannot be < 0V") 

    if not isinstance(channel, bool):
        sys.exit("Choose the right channel:\nFalse - 1st channel\nTrue - 2nd channel")

    
    #confugure the channel
    AO.nodeEnableSet(channel, AO.NODE.CARRIER, True)
    AO.nodeFunctionSet(channel, AO.NODE.CARRIER, AO.FUNC.SINE)
    AO.nodeFrequencySet(channel,AO.NODE.CARRIER, frequency)
    AO.nodeAmplitudeSet(channel, AO.NODE.CARRIER, amplitude)
    # AO.nodeOffsetSet(channel, AO.NODE.CARRIER, 0)
    
    # Run
    AO.configure(channel, True)
    
    # break
    print("Press Enter to exit")
    while True:
        breaker = input()
        if not breaker:
            break


#######################################################################################
#######################################################################################
#GetP2P
#######################################################################################
#######################################################################################

def GetP2P(averagingBufferSize: int, channel: bool, scope):

    # Check input values
    
    if not isinstance(averagingBufferSize, int):
        sys.exit("avarangingBufferSize should be integer value")
    
    if averagingBufferSize < 0:
        sys.exit("averagingBufferSize should couldn't be negative")

    if averagingBufferSize > 8192:
        sys.exit("max buffer size is 8192")
    
    if not isinstance(channel, bool):
        sys.exit("Choose the right channel:\nFalse - 1st channel\nTrue - 2nd channel")
    
    
    # set up acquisition
    scope.frequencySet(1e8)
    scope.bufferSizeSet(averagingBufferSize)
    scope.channelEnableSet(channel, True)
    scope.channelRangeSet(-25, 25)

    # begin acquisition
    scope.configure(False, True)
    
    # buffer fullness check
    while True:
        sts = scope.status(True)
        if sts == scope.STATE.DONE:
            break
        time.sleep(1e-7)  

    # peak to peak value
    P2P = max(scope.statusData(channel, averagingBufferSize)) - min(scope.statusData(channel, averagingBufferSize))
    
    return P2P

    
