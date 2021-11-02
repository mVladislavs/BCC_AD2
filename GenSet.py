def GenSet(frequency:int, amplitude:float, chanel:bool):

    import dwf
    import sys

    if frequency > 5e7:
        sys.exit("Frequency cannot be > 50MHz")
    
    elif frequency < 0:
        sys.exit("Frequency cannot be < 0Hz") 
    
    elif amplitude > 5:
        sys.exit("Amplitude cannot be > 5V")

    elif amplitude < 0:
        sys.exit("Amplitude cannot be < 0V")        

    AO = dwf.DwfAnalogOut()  #open device as analog outpput

    AO.nodeEnableSet(chanel, AO.NODE.CARRIER, True)
    AO.nodeFunctionSet(chanel, AO.NODE.CARRIER, AO.FUNC.SINE)
    AO.nodeFrequencySet(chanel,AO.NODE.CARRIER, frequency)
    AO.nodeAmplitudeSet(chanel, AO.NODE.CARRIER, amplitude)
    # AO.nodeOffsetSet(CHANNEL, AO.NODE.CARRIER, 0)

    print("Press Enter to exit")
    while True:
        AO.configure(chanel, True)
        breaker = input()
        if not breaker:
            break
    AO.close()