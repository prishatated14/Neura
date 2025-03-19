import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') #getting details of current voice
    engine.setProperty('voice', voices[1].id) #changing index, changes voices. 1 for female & changing index, changes voices. o for male
    engine.setProperty('rate', 174)     # setting up new voice rate
    print(voices)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer() #variable initialised using recognizer 
    
    with sr.Microphone() as source:   # mic is used as a source to detect speech
        print('Listening...')
        eel.DisplayMessage('listening...')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)

        audio=r.listen(source, timeout=5, phrase_time_limit=8) 
    try:
        print('recognizing')
        eel.DisplayMessage('recognizing...')
        query= r.recognize_google(audio, language='en-in') #recognize_google is standard engine of recognize
        print(f"user said:{query}")  
        eel.DisplayMessage(query)
        speak(query) 
        eel.ShowHood()
    except Exception as e: 
        print(f"Error: {e}")
        eel.DisplayMessage("Sorry, I didn't catch that. Please try again.")  # Handle errors 
        return ""
    return query.lower()

   
