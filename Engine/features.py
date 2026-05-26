from shlex import quote
from sqlite3 import Cursor
import struct
import subprocess
import sys
import os
import time

import pvporcupine
import pyaudio
import pyautogui

#from Engine.helper import extract_yt_term, remove_words





sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import playsound as playsound
import eel
from Engine.config import ASSISTANT_NAME
import pywhatkit as kit

@eel.expose
def speak(text):
    print(f"Speaking: {text}")


@eel.expose
def openCommand(query):
    query = query.lower()
    query = query.replace(ASSISTANT_NAME.lower(), "")
    query = query.replace("open", "").strip()

    app_map = {
        "chrome": "Google Chrome",
        "brave": "Brave Browser",
        "safari": "Safari",
        "vscode": "Visual Studio Code",
        "notes": "Notes"
    }

    app_name = app_map.get(query, query)  # fallback to raw query

    if app_name:
        speak(f"Opening {query}")
        print(f"Running command: open -a \"{app_name}\"")
        os.system(f"open -a \"{app_name}\"")
    else:
        speak("Please specify what you want to open")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
        # Add your code to play on YouTube here
    else:
        speak("Sorry, I couldn't understand what to play on YouTube.")

def extract_yt_term(command):
    import re
    pattern = r"(?:play|search)\s+(.*)"
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


#whatsapp message sending

def findcontact(query):

    #word_to_remove = [ASSISTANT_NAME, 'make', 'a' ,'to', 'phone' ,'call' ,'send', 'message', 'whatsapp', 'on', 'whatsapp', 'video']
   # query = remove_words(query, word_to_remove)

    try:
        query = query.strip().lower()
        Cursor.execute("SELECT mobile_no FROM Contact WHERE lower(name) Like ? OR Lower(name) Like ?", ('%' + query + '%', '%' + query + '%'))
        result = Cursor.fetchall()
        print(result[0][0])
        mobile_number_str = str(result[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str , query
    except:
        speak('not exist in conatact')
        return 0 ,0 
    
def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        Fido_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        Fido_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        Fido_message = "staring video call with "+name

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('command', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(Fido_message)
    
# def hotword():
#     porcupine = None
#     paud = None
#     audio_stream = None
#     try:
#         # Check available keywords first: print(pvporcupine.KEYWORDS)
#         porcupine = pvporcupine.create(keywords=["computer", "alexa"])  

#         paud = pyaudio.PyAudio()
#         audio_stream = paud.open(
#             rate=porcupine.sample_rate,
#             channels=1,
#             format=pyaudio.paInt16,
#             input=True,
#             frames_per_buffer=porcupine.frame_length
#         )

#         print("Listening for hotword on Mac...")

#         while True:
#             pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
#             pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
#             keyword_index = porcupine.process(pcm)

#             if keyword_index >= 0:
#                 print("Hotword detected!")

#                 # Example: trigger Command+Space (Spotlight on macOS)
#                 pyautogui.hotkey("command", "space")
#                 time.sleep(1)

#     except Exception as e:
#         print("Error:", e)
#     finally:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()



import os
import google.generativeai as genai

# Configure Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "ApI_key")
genai.configure(api_key=GEMINI_API_KEY)

# Create chatbot session
model = genai.GenerativeModel("gemini-2.5-flash")  
chat = model.start_chat(history=[])

def speak(text):
    print("[TTS] Speaking:", text)

def chatBot(query: str) -> str:
    if not query:
        return ""
    try:
        response = chat.send_message(query)
        reply = response.text
    except Exception as e:
        print("chat error", e)
        reply = "I couldn't reach the assistant service."
    # update frontend and (optionally) speak
    try:
        eel.receiverText(reply)
    except Exception:
        pass
    print("FIDO:", reply)
    speak(reply)
    return reply






# Example usage
#chatBot("Hello FIDO, how are you?")


#print(pvporcupine.KEYWORDS)

