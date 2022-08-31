import numpy as np
import glob
import os
import pandas as pd
from scipy import signal
from scipy.signal import waveforms
from matplotlib import pyplot as plt
tangent = 48
cutoff = 30e6

os.mkdir("lowpass")

file = glob.glob('*.csv')

wd =[]
otaniwd = []

#大谷窓　関数
def otaniwd(wave,ratio):#前後何パーセントにハン窓か(10%なら0.1)
    otani =[]
    L = len(wave)
    wd = 0.5-0.5*np.cos(((2*np.pi)*np.arange(0,ratio*2*L+1))/(ratio*2*L))
    ones  = np.ones(int((1-ratio*2)*L-1))
    otani = np.append(otani,wd[0:int(ratio*L)])
    otani = np.append(otani,ones)
    otani = np.append(otani,wd[int(ratio*L):int(ratio*2*L+1)])
    
    return wave*otani

#lowpass filter
def lpf(wave, cutoff, tangent,df):
    decay =[]
    
    FFT = np.fft.rfft(wave)
    f = np.arange(0,L/2+1)*df
    cutp = np.int16(cutoff/df)
    decay = np.append(decay,np.ones(cutp))
    decay = np.append(decay,np.power(f[cutp:]/cutoff,-1*tangent/np.log(2)))
    
    FFT = FFT[:int(L/2)+1]
    FFT = FFT*decay
    #iDFT
    return np.fft.irfft(FFT)



for i in file:
    #読み込み
    time = pd.read_csv(i,header=None,usecols = [0])
    time= time.iloc[:,0]#datalame型を変換
    wave = pd.read_csv(i,header = None,usecols = [1])
    wave = wave.iloc[:,0]

    L = len(wave)
    dt = time[2] - time[1]
    df = 1/(dt*L)

    #大谷窓
    wave = otaniwd(wave,0.1)
    
    #lowpass filter
    wave = lpf(wave, cutoff, tangent, df)

    data = pd.DataFrame(np.transpose([time,wave]))
    data.to_csv("lowpass/re_%s" % i, index=False,header =False)