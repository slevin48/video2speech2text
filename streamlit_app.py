import streamlit as st
import pytube
import moviepy.editor as mp
import speech_recognition as sr
import os

try:
    os.mkdir(os.mkdir('downloads'))
except OSError as error:
    print(error)

st.title('Video 2 Speech 2 Text')

# Steve Jobs' 2005 Stanford Commencement Address
# https://www.youtube.com/watch?v=UF8uR6Z6KLc
url = 'https://www.youtube.com/watch?v=UF8uR6Z6KLc'

url = st.text_input('Youtube URL',url)

dl = st.button('Download')


if dl:
    # Download Youtube video
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    # or
    # video = youtube.streams.get_highest_resolution()
    title = video.title
    path = video.download('downloads')
    st.text(title)
    st.video(path,format='video/mp4', start_time=0)

    # Video to Audio
    print(path)
    my_clip = mp.VideoFileClip(path)
    duration = my_clip.duration
    # my_clip.audio.write_audiofile("downloads/"+title+".wav")
    my_clip.audio.write_audiofile("downloads/speech.wav")
    st.text("Duration: "+str(duration))
    st.audio("downloads/speech.wav", format='audio/wav')

    # ## Speech to text
    r = sr.Recognizer()
    # break in 60 sec intervals
    audioFile = sr.AudioFile("downloads/speech.wav")
    i = 0
    audiolist = []
    while i*60 < duration:
        with audioFile as source:
            audio = r.record(source, offset=i*60, duration=60)
            audiolist.append(audio)
        i += 1
    
    with open("downloads/speech.txt","w") as f:
        for audio in audiolist:
            txt = r.recognize_google(audio)
            f.write(txt)
            st.text(txt)


    st.markdown('<a href="downloads/speech.txt">speech.txt</a>',unsafe_allow_html=True)
