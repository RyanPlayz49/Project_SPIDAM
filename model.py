import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from scipy.io import wavfile
from pydub import AudioSegment


class Model:
    def __init__(self):
        self.wav_name = ''

    # create the root window
    root = tk.Tk()
    root.title('Open File Dialog')
    root.resizable(False, False)
    root.geometry('300x150')

    def select_file(self):
        filetypes = (('wav files', '*.wav'), ('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
        if filename:  # Check if a file was selected
            self.wav_name = filename

            showinfo(title='Selected File', message=filename)
            wav_name_label = ttk.Label(self.root, text=self.wav_name)
            wav_name_label.pack(side="bottom")

            if self.wav_name.endswith(".wav"):
                samplerate, data = wavfile.read(self.wav_name)
                length = data.shape[0] / samplerate
                print(f"Num channels: {data.shape[len(data.shape) - 1]}")
                print(f"Sample Rate: {samplerate} Hz")
                print(f"Length: {length}s")
            else:
                audio = AudioSegment.from_file(self.wav_name)
                if audio.channels > 1:
                    audio = audio.set_channels(1)
                self.wav_name = "converted.wav"  # Set a new WAV file name
                audio.export(self.wav_name, format="wav")

    def create_GUI(self):
        self.root = tk.Tk()
        self.root.title('Open File Dialog')
        self.root.resizable(False, False)
        self.root.geometry('300x150')

        # Open button
        open_button = ttk.Button(self.root, text='Open a File', command=self.select_file)
        open_button.pack(expand=True)

        self.root.mainloop()

    def get_selected_file_path(self):
        return self.wav_name


# Usage
model_instance = Model()
model_instance.create_GUI()

selected_file_path = model_instance.get_selected_file_path()
if selected_file_path and os.path.exists(selected_file_path):
    print("Selected file path:", selected_file_path)
else:
    print("No valid file path selected or file doesn't exist.")
