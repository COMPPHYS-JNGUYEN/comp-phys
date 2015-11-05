import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io.wavfile import write
import copy
import os

class Tone:
    def __init__(self, f=0, dur=0, sr=44100, signal=0, orig_signal=0, overtones={}, OT_num=0):
        self.f = f
        self.dur = dur
        self.sr = sr
        self.signal = signal
        self.orig_signal = orig_signal
        self.overtones = overtones
        self.OT_num = OT_num
    
    def get_tone(self, f, dur, play_sound=False):
        self.f = f
        self.dur = dur
        time_pts = np.linspace(0, self.dur, self.dur*self.sr)
        amp = 2**10
        self.orig_signal = np.int16(amp*np.sin(np.pi*2*self.f*time_pts))
        if play_sound == True:
            self.playsound(outside_signal=self.orig_signal)
        return self.orig_signal
    
    def get_overtone(self, multi, play_sound=None):
        OT_f = multi*self.f
        time_pts = np.linspace(0, self.dur, self.dur*self.sr)
        amp = 2**10
        OT_signal = np.int16(amp*np.sin(np.pi*2*OT_f*time_pts))
        self.overtones[OT_f] = OT_signal
        self.OT_num += 1
        if play_sound == True:
            self.playsound(outside_signal=OT_signal)
        return None

    def playsound(self, outside_signal=None, sample_rate=44100, vol=0.05):
        if outside_signal == None:
            write('tmp.wav', self.sr, self.signal)
            os.system("afplay tmp.wav")
            os.system("rm tmp.wav")
        else:
            write('tmp.wav', self.sr, outside_signal)
            os.system("afplay tmp.wav")
            os.system("rm tmp.wav")

    def comb_tones(self):
        OT_weights = range(OT_num)
        for elem in OT_weights:
            OT_weights[elem] = raw_input('Please enter weight for overtone {:d}:

    def plot_fourier(self,sample_rate=44100, freq_lim=2000., amp_lim=1e7):
        ft = np.fft.fft(signal)
        freq = np.fft.fftfreq(signal.shape[0], d = 1./sample_rate)

        plt.figure()
        plt.plot(freq, ft.real, 'b-')
        plt.xlim([-1000, 1000])
        plt.figure()
        plt.plot(freq, ft.imag, 'g-')
        plt.xlim([-1000, 1000])
        plt.show()

        return ft, freq



#def equalizer(sample_rate, sound, wt1 = None, wt2 = None, wt3 = None, vol = 1.):
#    if wt1==None or wt2==None or wt3==None:
#    return sound
#    ft = np.fft.fft(sound)
#    freq = np.fft.fftfreq(sound.shape[0], d = 1./sample_rate)
#    filt1 = np.abs(freq) < 500
#    filt2 = (np.abs(freq)>500)*(np.abs(freq)<1000)
#    filt3 = np.abs(freq)>1000
#
#    band1 = signal_rec(ft, filt=filt1)
#    band2 = signal_rec(ft, filt=filt2)
#    band3 = signal_rec(ft, filt=filt3)
#
#    normalize = 1/((wt1**2)+(wt2**2)+(wt3**2))**.5
#    wt1 = wt1*normalize
#    wt2 = wt2*normalize
#    wt3 = wt3*normalize
#
#    new_sound = wt1*band1 + wt2*band2 + wt3*band3
#    return new_sound

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