import cohere
import speech_recognition
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

co = cohere.Client("fc77mWLmwJQQPUMFzHPKeMTAQTjbHoFrcq0JlhXf")

cohere_chat_res_start = co.chat("")
conv_session_id = cohere_chat_res_start.session_id


def respond(prompt):
    response = co.chat(prompt, session_id=conv_session_id, model="command-xlarge-beta", return_chatlog=True)
    return response.reply


def stt():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            playsound("1100_vELs219S.wav")
            state = "Listening"
            print("Listening")
            audio = recognizer.listen(source)
            result = recognizer.recognize_google(audio)
        return result
    except speech_recognition.UnknownValueError:
        print("Error with stt")
    except speech_recognition.RequestError:
        print("Request Error with stt")

def tts(text):
    tts = gTTS(text=text, tld="us")
    tts.save("audio.mp3")
    playsound("audio.mp3")
    os.remove("audio.mp3")


# ai_response = respond("Whatcha name?")
# print(ai_response)
