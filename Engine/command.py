import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    text = str(text)
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[14].id)  # use voices[0] for safety
    engine.setProperty('rate', 150)
    eel.DisplayMessage(text)
    eel.receiverText(text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")  # Display message in the frontend
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return ""

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        speak(query)  # Speak the recognized query
        time.sleep(1)  # Allow time for the message to be displayed
        
        

    except sr.UnknownValueError:
        print("Could not understand the audio, please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Speech recognition service failed; {e}")
        return ""

    return query.lower()


@eel.expose
def allCommands(message=1):

    if message == 1:
        query = take_command()
        print(query)
        eel.senderText(query or "")
    else:
        query = message
        eel.senderText(query)
    try:

        from Engine.features import chatBot
        reply = chatBot(query)
        if reply:
            eel.receiverText(reply)

        if "open" in query:
            from Engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from Engine.features import PlayYoutube
            PlayYoutube(query)
        
        elif "send message" in query or "phone call" in query or "video call" in query:
            from Engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = take_command()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = take_command()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = take_command()
                                        
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)

        else:
            from Engine.features import chatBot
            chatBot(query)

    except Exception as e:
        print("error", e)
        eel.receiverText("Sorry, an error occurred.")
    
    
    eel.ShowHood()



