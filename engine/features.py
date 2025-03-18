from playsound import playsound  
import eel

# Playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"  # Path to your sound file
    playsound(music_dir)  # Call the playsound function