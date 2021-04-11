import streamlit as st
import pytube
import moviepy.editor as mp
import speech_recognition as sr
import os, base64

try:
    os.mkdir(os.mkdir('downloads'))
except OSError as error:
    print(error)

st.title('Video 2 Speech 2 Text')

# 2 modes: youtube or local
src = st.radio("Youtube Download or Local Upload",["Download","Upload"])
st.write(src)
if src == "Upload":
    up = st.file_uploader("Upload a video", type=["mp4"])

    if up is not None:
        with open(os.path.join("downloads",up.name),"wb") as f:
            f.write(up.getbuffer())
        st.video(up,format='video/mp4', start_time=0)
        path = 'downloads/'+up.name
else:
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

try:
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

    data = open("downloads/speech.txt", "r").read()
    b64 = base64.b64encode(data.encode('ascii'))
    st.markdown(f'<a href="data:file/txt;base64,{b64}" download="speech.txt">speech.txt</a>',unsafe_allow_html=True)
except NameError:
    print('No video to process')