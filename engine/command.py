import pyttsx3
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') #getting details of current voice
    engine.setProperty('voice', voices[1].id) #changing index, changes voices. 1 for female & changing index, changes voices. o for male
    engine.setProperty('rate', 174)     # setting up new voice rate
    print(voices)
    engine.say(text)
    engine.runAndWait()

def takecommnad():
    r = sr.Recognizer() #variable initialised using recognizer 
    
    with sr.Microphone() as source:   # mic is used as a source to detect speech
        print('Listening...')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)

        audio=r.listen(source, 10, 6) #if listen it should listen for atleast 10s and if speaking it should capture voice for atleast 6s
    try:
        print('recognizing')
        query=r.recognize_google(audio, language='en-in') #recognize_google is standard engine of recognize
        print(f"user said:{query}")   
    except Exception as e:  
        return ""
    return query.lower()

text= takecommnad()

speak(text)    
