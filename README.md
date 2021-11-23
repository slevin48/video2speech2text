# video2speech2text 

*(project continued on [video-analyzer](https://github.com/slevin48/video-analyzer))*

Extract the audio from a video - then translate to text

**Demo:** Steve Jobs' 2005 Stanford Commencement Address

https://www.youtube.com/watch?v=UF8uR6Z6KLc

**Result:**
"this program is brought to you by Stanford University please visit us at stanford.edu thank you i'mma honoured to be with you today for your commencement from one of the finest universities in the world truth be told I never from college and this is the closest I've ever gotten to a College graduation today I want to tell you three stories from my life that's it no big deal just three stories the first story is about connecting the dots"

[full transcript](steve.txt)

**Features:**

- Download transcript as text file

https://user-images.githubusercontent.com/12418115/121565644-f26c2200-ca1c-11eb-8669-67b256792828.mp4

- Upload video from local file

https://user-images.githubusercontent.com/12418115/121565751-10d21d80-ca1d-11eb-85e5-bfcbb2ab6d49.mp4

**Convert WAV to MP3**
```python
from os import path
from pydub import AudioSegment

src = "steve.mp3"
dst = "steve.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
```


## Resources
- https://dev.to/seijind/how-to-download-youtube-videos-in-python-44od
- https://towardsdatascience.com/the-easiest-way-to-download-youtube-videos-using-python-2640958318ab
- https://towardsdatascience.com/extracting-audio-from-video-using-python-58856a940fd
- https://www.geeksforgeeks.org/moviepy-getting-duration-of-video-file-clip/
- https://fr.mathworks.com/help/vision/ref/vision.videofilereader-system-object.html
- https://pythonbasics.org/convert-mp3-to-wav/
- https://realpython.com/python-speech-recognition/
- https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
