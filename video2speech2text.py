# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# Video 2 Speech 2 Text

# %%
import os
os.mkdir('downloads')

# %%
# Steve Jobs' 2005 Stanford Commencement Address
# https://www.youtube.com/watch?v=UF8uR6Z6KLc
url = 'https://www.youtube.com/watch?v=UF8uR6Z6KLc'


# %%
import pytube
youtube = pytube.YouTube(url)


# %%
video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()
# or
# video = youtube.streams.get_highest_resolution()
title = video.title


# %%
path = video.download('downloads')

# %%
import moviepy.editor as mp


# %%
import os
dl = os.listdir("downloads")
dl


# %%
my_clip = mp.VideoFileClip(path)


# %%
my_clip


# %%
duration = my_clip.duration
duration


# %%
# my_clip.audio.write_audiofile("downloads/"+title+".wav")
my_clip.audio.write_audiofile("downloads/speech.wav")


# %%
# ## Speech to text
import speech_recognition as sr
sr.__version__


# %%
r = sr.Recognizer()


# %%
# audioFile = sr.AudioFile("downloads/"+title+".wav")
# audioFile = sr.AudioFile("downloads/speech.wav")
# with audioFile as source:
#    audio = r.record(source, duration=60)


# # %%
# txt = r.recognize_google(audio)
# txt


# # %%
# with open("downloads/speech.txt","w") as f:
#     f.write(txt)


# %%
# break in 60 sec intervals
audioFile = sr.AudioFile("downloads/speech.wav")
i = 0
audiolist = []
while i*60 < duration:
    with audioFile as source:
        audio = r.record(source, offset=i*60, duration=60)
        audiolist.append(audio)
    i += 1


# %%
with open("downloads/speech.txt","w") as f:
    for audio in audiolist:
        txt = r.recognize_google(audio)
        f.write(txt)

