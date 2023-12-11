import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from scipy.io import wavfile
from pydub import AudioSegment


# Creates Model class
class Model:

    # Defines variable being used to store .wav file name
    def __init__(self):
        self.root = None
        self.wav_name = ''

    # Creates the root window

    # Creates function that helps find and insert .wav file into program
    def select_file(self):
        filetypes = (('wav files', '*.wav'), ('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
        if filename:  # Checks if a file was selected
            self.wav_name = filename

            showinfo(title='Selected File', message=filename)
            wav_name_label = ttk.Label(self.root, text=self.wav_name)
            wav_name_label.pack(side="bottom")

            if self.wav_name.endswith(".wav"):  # Checks if file ends in .wav
                samplerate, data = wavfile.read(self.wav_name)
                length = data.shape[0] / samplerate
                print(f"Num channels: {data.shape[len(data.shape) - 1]}")
                print(f"Sample Rate: {samplerate} Hz")
                print(f"Length: {length}s")
            else:  # Converts file to .wav if it is not already a .wav
                audio = AudioSegment.from_file(self.wav_name)
                if audio.channels > 1:  # Checks if .wav file has more than 1 channel and compresses it if it is more than 1
                    audio = audio.set_channels(1)
                self.wav_name = "converted.wav"  # Set a new WAV file name
                audio.export(self.wav_name, format="wav")

    # Function to create window to choose files from file explorer on home screen of device
    def create_GUI(self):
        self.root = tk.Tk()
        self.root.title('Open File Dialog')
        self.root.resizable(False, False)
        self.root.geometry('300x150')

        # Open button
        open_button = ttk.Button(self.root, text='Open a File', command=self.select_file)
        open_button.pack(expand=True)

        # Show button
        show_button = ttk.Button(self.root, text='Show Data', command=self.show_data)
        show_button.pack(expand=True)

        self.root.mainloop()

    # Function to open a new window that shows data
    def show_data(self):

        samplerate, data = wavfile.read(self.wav_name)
        length = data.shape[0] / samplerate

        channel_label = tk.Label(text=f"Num channels: {data.shape[len(data.shape) - 1]}")
        samplerate_label = tk.Label(text=f"Sample Rate: {samplerate} Hz")
        length_label = tk.Label(text=f"Length: {length}s")

        channel_label.pack()
        samplerate_label.pack()
        length_label.pack()

    # Returns .wav file name
    def get_selected_file_path(self):
        return self.wav_name


# Usage
model_instance = Model()
model_instance.create_GUI()

selected_file_path = model_instance.get_selected_file_path()
if selected_file_path and os.path.exists(
        selected_file_path):  # Checks if selected file is a .wav file and prints name to console
    print("Selected file path:", selected_file_path)
else:
    print("No valid file path selected or file doesn't exist.")
