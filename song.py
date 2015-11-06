""" Program uses class Tone to generate tones with particular fundamental frequencies.  It also creates overtones and combines them
with the original tone to create a signal or sound.  This program plots the fourier transform of the combined signal, both its
real and imaginary parts as well as plots the combined tone against time.  An example is provided below of how the program works,
playing part of the nursery rhyme, Mary had a Little Lamb.  The program also demonstrates the working methods inside the class, Tone.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io.wavfile import write
import copy
import os

class Tone:
    def __init__(self, f=0, dur=0, sr=44100, signal=0, orig_signal=0, overtones={}, OT_num=0):          # Intializing attributes inside class.
        self.f = f                          # Frequency
        self.dur = dur                      # Duration
        self.sr = sr                        # Sampling Rate
        self.signal = signal                # Numpy array that stores the tone plus the overtones.
        self.orig_signal = orig_signal      # Numpy array that stores the simple one-frequency tone with frequency f_1.
        self.overtones = overtones          # Dictionary that stores the overtones.
        self.OT_num = OT_num                # Number of overtones present.
    
    def get_tone(self, f, dur, play_sound=False):       # Generates a tone at the given fundamental frequency.
        self.f = f
        self.dur = dur
        time_pts = np.linspace(0, self.dur, self.dur*self.sr)
        amp = 2**10
        self.orig_signal = np.int16(amp*np.sin(np.pi*2*self.f*time_pts))        # Creates original signal with the fundamental frequency
        if play_sound == True:                          # Plays self.orig_signal if True.
            self.playsound(outside_signal=self.orig_signal)
        return self.orig_signal
    
    def get_overtone(self, multi, play_sound=None):     # Generates an overtone that has a frequency that is multi*f.
        OT_f = multi*self.f              # Overtone frequency
        time_pts = np.linspace(0, self.dur, self.dur*self.sr)
        amp = 2**10
        OT_signal = np.int16(amp*np.sin(np.pi*2*OT_f*time_pts))     # New overtone signal from multiplied frequency.
        self.overtones[OT_f] = OT_signal            # Add the overtone frequency and overtone signal to self.overtones, a dictionary of overtones and corresponding numpy arrays.
        self.OT_num += 1
        if play_sound == True:
            self.playsound(outside_signal=OT_signal)
        return None

    def comb_tones(self):       # Combines the tone at the fundamental frequency and all overtones present.
        normalize = 0       # Intialize normalization factor
        OT_weights = self.overtones.copy()      # Used so OT_weights does not point at the same object as self.overtones.
        for i in OT_weights:        # Overwrites values in OT_weights with desired weighting for particular overtones.
            OT_weights[i] = int(raw_input('Please enter weight for overtone {:f}: '.format(i)))
        for key in OT_weights:      # Taking a step in the normalization process, squaring the values of the desired weights.
            normalize += OT_weights[key]**2
        normalize **= .5            # Final step to find the normalization factor.
        for key in OT_weights:      # Normalizes values associated to keys in dictionary OT_weights.  Then adds the weights times the numpy arrays of self.overtones[key] to self.signal.
            OT_weights[key] = OT_weights[key]/normalize
            self.signal += OT_weights[key]*self.overtones[key]
        return self.signal

    def playsound(self, outside_signal=None, sample_rate=44100, vol=0.05):      # Pplays the combined tone.
        if outside_signal == None:
            write('tmp.wav', sample_rate, np.int16(vol*self.signal))
            os.system("afplay tmp.wav")
            os.system("rm tmp.wav")
        else:
            write('tmp.wav', sample_rate, outside_signal)
            os.system("afplay tmp.wav")
            os.system("rm tmp.wav")

    def plot_fourier(self, sample_rate=44100, freq_lim=2000., amp_lim=1e7):     # Plots the real and imaginary parts of the DFT of the combined tone.
        ft = np.fft.fft(self.signal)        # Fourier transforms the combined signal.
        freq = np.fft.fftfreq(self.signal.shape[0], d = 1./sample_rate)     # Creates the frequency associated with the combined signal.

        plt.figure()        # Plots the real part of the Fourier transform.
        plt.plot(freq, ft.real, 'b-')
        plt.title('Real Part of Fourier Transform')
        plt.xlim([-freq_lim, freq_lim])
        plt.ylim([-amp_lim, amp_lim])
        plt.figure()        # Plots the imaginary part of the Fourier transform.
        plt.plot(freq, ft.imag, 'g-')
        plt.title('Imaginary Part of Fourier Transform')
        plt.xlim([-freq_lim, freq_lim])
        plt.ylim([-amp_lim, amp_lim])
        plt.show()

    def plot_sound(self, t_lim=0.02):       # Plots the combined tone against time.
        time = np.linspace(0, self.dur, self.dur*self.sr)
        plt.figure()        # Plots the combined signal against time.
        plt.title("Sound Wave vs. Time")
        plt.plot(time, self.signal)
        plt.xlim([0, t_lim])
        plt.show()


fund1 = Tone()      # Instantiation of the four fundamental frequencies.
fund2 = Tone()
fund3 = Tone()
fund4 = Tone()

A = fund1.get_tone(440., .5)          # A tone
B = fund2.get_tone(493.88, .5)        # B tone
D = fund3.get_tone(587.33, .5)        # D tone
G = fund4.get_tone(392., .5)          # G tone

##################################################################################################################
# Testing fundamental frequency 1 (440 Hz, A tone) demonstrating that the methods in class, Tone, work.

fund1.get_overtone(2)
fund1.get_overtone(3)
fund1.get_overtone(4)
f1_rich = fund1.comb_tones()

print "For A tone, the frequency, sampling_rate, duration, and number of overtones are:",\
        fund1.f, ',', fund1.sr, ',', fund1.dur, ',', fund1.OT_num

fund1.playsound()
fund1.plot_sound()
fund1.plot_fourier(freq_lim=2000.)

##################################################################################################################

melody = np.concatenate(np.array([B, A, G, A, B, B, B, B, A, A, A, A]))     # Mary Had a Little Lamb nursery rhyme numpy array.
mel = Tone()        # Instantiation of mel into class Tone.
mel.playsound(outside_signal=melody)        # Plays Mary Had a Little Lamb nursery rhyme, corresponding to variable, melody.
