import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from scipy.io import wavfile
import scipy.io
from pydub import AudioSegment


wav_name = ''
# create the root window
root = tk.Tk()
root.title('Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('wav files', '*.wav'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    wav_name = filename
    # tkinter.messagebox — Tkinter message prompts
    showinfo(title='Selected File', message=filename)
    wav_name_label = ttk.Label(root, text=wav_name)
    wav_name_label.pack(side="bottom")


# open button
open_button = ttk.Button(root, text='Open a File', command=select_file)

open_button.pack(expand=True)

"""
root.mainloop()
samplerate, data = wavfile.read(wav_name)
length = data.shape[0] / samplerate
print(f"Num channels: {data.shape[len(data.shape) - 1]}")
print(f"Sample Rate: {samplerate} Hz")
print(f"Length: {length}s")
"""

if wav_name.format() != "wav":
    wav_name = AudioSegment.from_wav(wav_name)

if wav_name.channels() > 1:
    mono_wav = wav_name.set_channels(1)
    mono_wav.export(wav_name, format="wav")
    mono_wav_audio = AudioSegment.from_file(wav_name, format="wav")
