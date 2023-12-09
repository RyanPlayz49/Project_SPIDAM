import numpy as np
import wave
import matplotlib.pyplot as plt
from model import Model

# Creates Controller class
class Controller:

    # Defines and intializes variables being used in the file
    def __init__(self):
        model = Model()
        self.wav_name = model.get_selected_file_path()
        self.wav_obj = wave.open(self.wav_name, 'rb')
        self.wav_show = self.wav_obj.getframerate()
        print(self.wav_show)

        self.n_samples = self.wav_obj.getnframes()
        self.t_audio = self.n_samples / self.wav_show

        self.times = np.linspace(0, self.n_samples / self.wav_show, num=self.n_samples)
        signal_wave = self.wav_obj.readframes(self.n_samples)
        self.signal_array = np.frombuffer(signal_wave, dtype=np.int16)
        self.l_channel = self.signal_array[0::2]
        self.array = [self.signal_array.tolist()]

        self.plotAudio()

    # Defines function used to display graph of audio values
    def plotAudio(self):
        plt.figure(figsize=(15, 5))
        plt.plot(self.times, self.l_channel)
        plt.title('Sample.wav')
        plt.ylabel('Signal Value')
        plt.xlabel('Time (s)')
        plt.xlim(0, self.t_audio)
        plt.show()

    # Finds the highest value
    def getHighest(self, array):
        currentHighest = array[0]
        finalHighest = array[0]
        for i in range(0, int(len(array)) - 1):
            if array[i] > array[i + 1]:
                currentHighest = array[i]
            else:
                currentHighest = array[i + 1]
            if currentHighest > finalHighest:
                finalHighest = currentHighest
        return finalHighest

    # Finds lowest value
    def getLowest(self, array):
        currentLowest = array[0]
        finalLowest = array[0]
        for i in range(0, int(len(array)) - 1):
            if array[i] < array[i + 1]:
                currentLowest = array[i]
            else:
                currentLowest = array[i + 1]
            if currentLowest < finalLowest:
                finalLowest = currentLowest
        return finalLowest

    # Finds medium value
    def getMedium(self, array):
        medium = (self.getLowest(array) + self.getHighest(array)) / 2
        return medium

    # Function that calculates and plots graph of frequency values
    def plot_frequency(self):
        lowFreq = self.getLowest(self.array)
        midFreq = self.getMedium(self.array)
        highFreq = self.getHighest(self.array)

        amplitude = midFreq / highFreq
        dB_data = [20 * np.log10(abs(self.wav_name) / amplitude) for sample in self.array]

        index_of_lowFreq = np.where(dB_data == lowFreq)
        index_of_midFreq = np.where(dB_data == midFreq)
        index_of_highFreq = np.where(dB_data == highFreq)

        low_rt20 = (self.times[index_of_lowFreq])[0]
        mid_rt20 = (self.times[index_of_midFreq])[0]
        high_rt20 = (self.times[index_of_highFreq])[0]

        low_rt60 = 3 * low_rt20
        mid_rt60 = 3 * mid_rt20
        high_rt60 = 3 * high_rt20

        plt.plot(self.times[index_of_lowFreq], low_rt60)
        plt.plot(self.times[index_of_midFreq], mid_rt60)
        plt.plot(self.times[index_of_highFreq], high_rt60)

        plt.grid()
        plt.show()


controller_instance = Controller()
controller_instance.plotAudio()
controller_instance.plot_frequency()
