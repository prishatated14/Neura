from cmath import e
import re
import struct
from pipes import quote
import subprocess
import time
import webbrowser
from playsound import playsound  
import eel
import os
import sqlite3
import pvporcupine
import pyaudio
import pyautogui

from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
from engine.helper import extract_yt_term, remove_words 

# Playing assistant sound function
con = sqlite3.connect("neura.db")
cursor = con.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"  # Path to your sound file
    playsound(music_dir)  # Call the playsound function

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")    
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()  # remove spaces from start and end of query

    if app_name != "":
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)  # start brave
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term) 

def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    
    try:
        # Initialize Porcupine with custom wake word
        porcupine = pvporcupine.create(
            access_key="GLdm7mzmGtA7JDc5Y35EYTKIlYkBjbZskY+ahWGNYTfUt7n1YGwCYw==",
            keyword_paths=[r"C:\Users\lenovo\OneDrive\Desktop\neura\engine\neural\neural_en_windows_v3_0_0.ppn"],
            keywords=["alexa"]
        )
        
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
        
        # Continuous listening loop
        while True:
            # Read audio frame
            audio_frame = audio_stream.read(porcupine.frame_length)
            audio_frame = struct.unpack_from("h" * porcupine.frame_length, audio_frame)
            
            # Process audio frame
            keyword_index = porcupine.process(audio_frame)
            
            if keyword_index >= 0:
                print("Hotword detected!")
                
                # Execute command
                pyautogui.keyDown("win")
                pyautogui.press("n")
                time.sleep(0.1)
                pyautogui.keyUp("win")
    
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", 
                      ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0

def whatsApp(mobile_no, message, flag, name):
    try:
        if flag == 'message':
            target_tab = 12
            jarvis_message = "message send successfully to "+name
        elif flag == 'call':
            target_tab = 6
            message = ''
            jarvis_message = "calling to "+name
        else:
            target_tab = 5
            message = ''
            jarvis_message = "starting video call with "+name

        # Clean phone number (remove spaces and special chars)
        clean_number = ''.join(filter(str.isdigit, mobile_no))
        
        # Construct URL with cleaned number
        whatsapp_url = f"whatsapp://send?phone={clean_number}&text={quote(message)}"
        
        # Open WhatsApp just once (removed duplicate call)
        subprocess.run(f'start "" "{whatsapp_url}"', shell=True)
        time.sleep(3)  # Reduced from 5 seconds
        
        # Focus search and navigate
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        
        # More reliable tab navigation (using press instead of hotkey)
        for _ in range(target_tab):
            pyautogui.press('tab')
            time.sleep(0.2)  # Short delay between tabs
            
        time.sleep(0.5)
        pyautogui.press('enter')  # Single enter press is usually enough
        
        speak(jarvis_message)
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        speak(f"Failed to complete {flag} with {name}")
        return False