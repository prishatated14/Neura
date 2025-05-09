import struct
import time
import pvporcupine
import pyaudio
import pyautogui

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
        
        ##print("Listening for wake words... (Say 'neural' or 'alexa')")
        
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
                pyautogui.press("j")
                time.sleep(0.1)
                pyautogui.keyUp("win")
                
    
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


hotword()





    