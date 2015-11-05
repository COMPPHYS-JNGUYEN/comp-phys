import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io.wavfile import write
import copy
import os

class Tone:
    def __init__(self, f=0, dur=0, sr=0, signal=0,orig_signal=0, overtones={}, OT_num=0):
        self.f = f
        self.dur = dur
        self.sr = sr
        self.signal = signal
        self.orig_signal = orig_signal
        self.overtones = overtones
        self.OT_num = OT_num
        
    def get_tone(self, f, dur, play_sound=False):
        time_pts = np.linspace(0, dur, dur*self.sr)
        self.f = f
        amp = 2**10
        tone_data = np.int16(amp*np.sin(np.pi*2*f*time_pts))
        if play_sound == True:
            playsound(outside_signal=tone_data)
        return tone_data
    
    def playsound(self, outside_signal=None, sample_rate=44100, vol=0.05):
        if outside_signal == None:
            write('tmp.wav', sample_rate, self.signal)
            os.system("afplay tmp.wav") 
            os.system("rm tmp.wav") 
        else:
            write('tmp.wav', sample_rate, outside_signal)
            os.system("afplay tmp.wav") 
            os.system("rm tmp.wav") 
        return
        

        
        
tones = Tone()
print tones.f

# def playsound(rate, sndarr):
#     from scipy.io.wavfile import write
#     import os
#     write('tmp.wav', rate, sndarr)
#     os.system("afplay tmp.wav") 
#     os.system("rm tmp.wav") 
#     return

# def get_tone(f, duration, sample_rate=44100, amp=2**13, play_sound=False):
#     time_pts = np.linspace(0, duration, duration*sample_rate)
#     tone_data = np.int16(amp*np.sin(np.pi*2*f*time_pts))
#     if play_sound == True:
#         playsound(sample_rate, tone_data)
#     return tone_data

# def plot_fourier(sample_rate, signal, freq_lim=1000.):
#     ft = np.fft.fft(signal)
#     freq = np.fft.fftfreq(signal.shape[0], d = 1./sample_rate)

#     plt.figure()
#     plt.plot(freq, ft.real, 'b-')
#     plt.xlim([-1000, 1000])
#     plt.figure()
#     plt.plot(freq, ft.imag, 'g-')
#     plt.xlim([-1000, 1000])
#     plt.show()

#     return ft, freq