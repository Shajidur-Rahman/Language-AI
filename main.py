import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()

# input_language = 'bn-BD'
input_language = 'es-MS'
# input_language = 'ar-SA'
your_language = 'en'

try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_language)
        print(text)
except:
    pass

translator = googletrans.Translator()

translated = translator.translate(text, dest=your_language)
converted_audio = gtts.gTTS(translated.text, lang=your_language)
converted_audio.save("My_audio.mp3")
print(translated.text)
playsound.playsound("My_audio.mp3")
