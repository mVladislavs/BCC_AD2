def GetP2P(averagingBufferSize: int, channel: bool):
    import dwf
    import time
    import sys

    # Check input values
    if not isinstance(averagingBufferSize, int):
        sys.exit("avarangingBufferSize should be integer value")
    
    elif averagingBufferSize < 0:
        sys.exit("averagingBufferSize should couldn't be negative")

    elif averagingBufferSize > 8192:
        sys.exit("max buffer size is 8192")
    
    elif not isinstance(channel, bool):
        sys.exit("Choose the right channel:\nFalse - 1st channel\nTrue - 2nd channel")
    
    # open device
    scope = dwf.DwfAnalogIn()

    # set up acquisition
    scope.frequencySet(1e8)
    scope.bufferSizeSet(averagingBufferSize)
    scope.channelEnableSet(channel, True)
    scope.channelRangeSet(channel, 5)

    # begin acquisition
    scope.configure(channel, True)
    
    # buffer fullness check
    while True:
        sts = scope.status(True)
        if sts == scope.STATE.DONE:
            break
        time.sleep(1e-7)  

    # peak to peak value
    P2P = max(scope.statusData(channel, averagingBufferSize)) - min(scope.statusData(channel, averagingBufferSize))
    
    # Finish
    scope.close()
    return P2P
