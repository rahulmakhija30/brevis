import speech_recognition as sr
import os
from os import path
import pydub
from pydub import AudioSegment
from pydub.effects import normalize
from pydub.playback import play
from pydub.utils import which
import youtube_dl

AudioSegment.converter = which("ffmpeg")

def speech_to_text(url):
    if not os.path.exists('audio'):
        os.mkdir('audio')

    # Extract Audio From YouTube
    os.system('youtube-dl -f bestaudio --extract-audio --audio-format mp3 --output audio/test.mp3 --audio-quality 0 '+url)

    # convert mp3 file to wav
    sound = AudioSegment.from_file("audio/test.mp3")
    sound.export("audio/test.wav", format="wav")

    s = AudioSegment.from_file("audio/test.wav")
    s = s+10
    s = normalize(s)
    s.export("audio/test.wav",format="wav")
    # transcribe audio file
    AUDIO_FILE = "audio/test.wav" 

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

            text = r.recognize_google(audio)

            with open('transcript.txt' , 'w') as f:
                    f.write(text)

            return text
    
if __name__ == '__main__':
    url = input()
    text = speech_to_text(url)
    print(text)