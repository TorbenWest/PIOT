import pyaudio
import wave
import gtts
import speech_recognition as sr
import playsound
import time

def speak(text):
    tts = gtts.gTTS(text=text, lang='nl')
    filename = 'voice.mp3' #File waarin het text bestand staat
    tts.save(filename)
    playsound.playsound(filename) #Text bestand afspelen

def get_audio():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        print("wollah zegwat")
        r.adjust_for_ambient_noise(source) #Zorgt voor ruis vermindering
        audio = r.listen(source) #Gebruikt microfoon als luisterbron
        said = '' #Variabel aanmaken die staat voor hetgeen wat gezegd is
        
        try:
            said = r.recognize_google(audio) #Herkend wat gezegd wordt via google API
            print(said) #Print wat er gezegd is
        except Exception as e: #Als er niets word gezegd
            print("Exception: " + str(e))
    return said

naam = "jord"
while True:
    text = get_audio()
    if "hallo" in text:
        speak("hallo "+ str(naam))
    elif "Hallo" in text:
        speak("enne "+ str(naam))
    else:
        print("begrijp je niet")
    time.sleep(1)
