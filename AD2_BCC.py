import dwf
import sys
import time


class AD2:

    #######################################################################################
    ######################################################################################
    #Init
    #######################################################################################
    ######################################################################################


    def __init__(self):

        if len(dwf.DwfEnumeration()) == 0:
            sys.exit("No AD2 detected")

        hdwf_token = dwf.Dwf() # get token
        self.AO = dwf.DwfAnalogOut(hdwf_token) # open device as analog outpput 
        self.AIN = dwf.DwfAnalogIn(hdwf_token) # open device as analog input 
        

    #######################################################################################
    ######################################################################################
    #close
    #######################################################################################
    ######################################################################################

    def close(self):

        self.AIN.close() 
        self.AO.close()

    #######################################################################################
    ######################################################################################
    #GenSet
    #######################################################################################
    ######################################################################################

    def GenSet(self, frequency:int, amplitude:float, channel:int):

        ##Check input values
        # frequency
        if frequency > 5e7:
            sys.exit("Frequency cannot be > 50MHz")
        if frequency < 0:
            sys.exit("Frequency cannot be < 0Hz")
        
        #amplitude
        if amplitude > 5:
            sys.exit("Amplitude cannot be > 5V")
        if amplitude < 0:
            sys.exit("Amplitude cannot be < 0V") 

        #channel
        if not isinstance(channel, int):
            sys.exit("Use 0 or 1 to choose the channel")
        if channel > 1:
            sys.exit("Use 0 or 1 to choose the channel")
        if channel <0:
            sys.exit("Use 0 or 1 to choose the channel")

        gen = self.AO
        
        # Confugure the channel
        gen.nodeEnableSet(channel, gen.NODE.CARRIER, True)
        gen.nodeFunctionSet(channel, gen.NODE.CARRIER, gen.FUNC.SINE)
        gen.nodeFrequencySet(channel,gen.NODE.CARRIER, frequency)
        gen.nodeAmplitudeSet(channel, gen.NODE.CARRIER, amplitude)
        #AO.nodeOffsetSet(channel, AO.NODE.CARRIER, 0)
        
        # Run
        gen.configure(channel, True)


    #######################################################################################
    #######################################################################################
    #GetP2P
    #######################################################################################
    #######################################################################################

    def GetP2P(self, averagingBufferSize: int, channel: bool):

        ## Check input values
        # Buffer size
        if not isinstance(averagingBufferSize, int):
            sys.exit("avarangingBufferSize should be integer value")
        if averagingBufferSize < 0:
            sys.exit("averagingBufferSize should couldn't be negative")
        if averagingBufferSize > 8192:
            sys.exit("max buffer size is 8192")
        
        #Channel
        if not isinstance(channel, int):
            sys.exit("Use 0 or 1 to choose the channel")
        if channel > 1:
            sys.exit("Use 0 or 1 to choose the channel")
        if channel <0:
            sys.exit("Use 0 or 1 to choose the channel")
        
        scope = self.AIN
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

    
