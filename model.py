import numpy as np
import wave
import matplotlib.pyplot as plt
wav_obj = wave.open('sample.wav', 'rb')

wav_show = wav_obj.getframerate()
print (wav_show)

n_samples = wav_obj.getframerate()

t_audio = n_samples/n_samples

times = np.linspace(0, n_samples/wav_show, num=n_samples)
signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave,dtype=np.int16)

l_channel = signal_array[0::2]

plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Sample.wav')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()