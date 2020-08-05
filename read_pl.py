import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

#Read audio input
sampling_freq, audio = wavfile.read('input_read.wav')

#Print param
print('Shape:', audio.shape)
print('Datatype:', audio.dtype)
print('Duration:', round(audio.shape[0] / float(sampling_freq), 3), 'seconds')

#Normalize the 16-bit int data
audio = audio / (2.**15)

#Get the first 30 values for plot
audio30 = audio[:30]

#Build the time axis
x_values = np.arange(0, len(audio30), 1) / float(sampling_freq)

#Convert to sec
x_values *= 1000

#Plotting the cropped audio
plt.plot(x_values, audio30, color='blue')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.title('Audio30 signal')
plt.show()
