import dwf
import numpy as np
import time


 #constants
HZ_ACQ = 1e8
N_SAMPLES = 8000
time_step = HZ_ACQ/N_SAMPLES
frequency = 2e6
f1 = open("Buffer.csv", "w")
f2 = open("Spectrum.csv", "w")
f3 = open("Amplitude.csv", "w")


hdwf = dwf.Dwf()

dwf_ao = dwf.DwfAnalogOut(hdwf)
dwf_ao.nodeEnableSet(0, dwf_ao.NODE.CARRIER, True)
dwf_ao.nodeFunctionSet(0, dwf_ao.NODE.CARRIER, dwf_ao.FUNC.SINE)
dwf_ao.nodeFrequencySet(0, dwf_ao.NODE.CARRIER, frequency)
dwf_ao.nodeAmplitudeSet(0, dwf_ao.NODE.CARRIER, 1)
dwf_ao.configure(0, True)

 #set up acquisition
dwf_ai = dwf.DwfAnalogIn(hdwf)
dwf_ai.channelEnableSet(0, True)
dwf_ai.channelRangeSet(0, 5.0)
dwf_ai.acquisitionModeSet(dwf_ai.ACQMODE.SCAN_SHIFT)
dwf_ai.frequencySet(HZ_ACQ)
dwf_ai.bufferSizeSet(N_SAMPLES)

 #begin acquisition
dwf_ai.configure(False, True)


# HarmonicVector = np.fft.rfftfreq(N_SAMPLES, 1 / HZ_ACQ)
start = time.time()
TIME = 0
while TIME < 60:
    sts = dwf_ai.status(True)

    cValid = dwf_ai.statusSamplesValid()
    rgdSamples = dwf_ai.statusData(0, cValid)

    Spectrum = 2*np.abs(np.fft.rfft(rgdSamples)) / N_SAMPLES 
    Harmonic = int(frequency/HZ_ACQ * N_SAMPLES)
    SignalAmplitude = Spectrum[Harmonic]
    
    print(SignalAmplitude)
    noise = np.delete(Spectrum, Harmonic)
    noiseRMS = np.sqrt(np.mean)
    SNR = 20 * np.log(SignalAmplitude/noiseRMS)
    
    f1.writelines([rgdSamples])
    f2.writelines([Spectrum])
    f3.write(SignalAmplitude + SNR)

    time.sleep(0.1)
    TIME = TIME + 0.1


    print(SNR)
end = time.time()

ExecutionTime = end - start
print(ExecutionTime)
f1.close()
f2.close()
f3.close()

