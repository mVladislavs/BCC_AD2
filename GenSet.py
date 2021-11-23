def GenSet(frequency:int, amplitude:float, channel:bool):

    import dwf
    import sys

    # Check input values
    if frequency > 5e7:
        sys.exit("Frequency cannot be > 50MHz")
    
    elif frequency < 0:
        sys.exit("Frequency cannot be < 0Hz")
    
    elif amplitude > 5:
        sys.exit("Amplitude cannot be > 5V")

    elif amplitude < 0:
        sys.exit("Amplitude cannot be < 0V") 

    elif not isinstance(channel, bool):
        sys.exit("Choose the right channel:\nFalse - 1st channel\nTrue - 2nd channel")

    #open device as analog outpput
    AO = dwf.DwfAnalogOut()
    
    #confugure the channel
    AO.nodeEnableSet(channel, AO.NODE.CARRIER, True)
    AO.nodeFunctionSet(channel, AO.NODE.CARRIER, AO.FUNC.SINE)
    AO.nodeFrequencySet(channel,AO.NODE.CARRIER, frequency)
    AO.nodeAmplitudeSet(channel, AO.NODE.CARRIER, amplitude)
    # AO.nodeOffsetSet(channel, AO.NODE.CARRIER, 0)
    
    # Run
    AO.configure(channel, True)
    
    # Break
    print("Press Enter to exit")
    breaker = input()
    if not breaker:
        AO.close()
