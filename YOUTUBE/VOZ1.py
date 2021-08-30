import webbrowser
import speech_recognition as sr 
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Hola, soy tu asistente de voz: ")
    audio=r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print("Has dicho: {}".format(text))
        print(text)
        if "Amazon" in text:
            webbrowser.open('https://amazon.mx')
        if "Youtube" in text:
            webbrowser.open('https://youtube.com')
    except:
        print("No te he entendido")
        