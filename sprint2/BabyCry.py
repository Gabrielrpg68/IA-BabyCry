import pyttsx3, speech_recognition as sr



engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id) #brasil
engine.setProperty('volume', 1)
engine.setProperty("rate", 155)

#Processa as modificações feitas até o momento
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Ouve o usuario.
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n  Listening...\n")
        speak('ouvindo')
        r.adjust_for_ambient_noise = 1.25
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("  Recognizing...\n")
        speak('Espera um pouco pra eu tentar entender.')
        query = r.recognize_google(audio, language='pt')
        #print(query)
    except:
        return "©empty_^_^_queryª"
    return query



speak("Como posso ajudar hoje?")
if __name__ == "__main__":
    while True:

        query = command().lower()
        print(query)
        if 'tocar' in query or 'musica' in query or 'música' in query or 'ninar' in query:
            from playsound import playsound
            print("opção: 1 ")
            playsound('NanaNenem.mp3')

        elif 'vídeo' in query or 'mostrar' in query:
            import cv2
            captura = cv2.VideoCapture("NanaNenemVideo.mp4")

            while (1):
                ret, frame = captura.read()
                cv2.imshow("Video", frame)

                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break
            captura.release()
            cv2.destroyAllWindows()

        elif 'temperatura' in query or 'qual' in query or 'paulo' in query:
            import requests
            API_KEY = "fa05b77c58d590636ee8c060fc0706db"
            cidade = "são paulo"
            link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"

            requisicao = requests.get(link)
            requisicao_dic = requisicao.json()
            descricao = requisicao_dic['weather'][0]['description']
            temperatura = requisicao_dic['main']['temp'] - 273.15
            temperatura = round(temperatura, 2)
            print(descricao, f"{temperatura}°C")
            speak(f"São Paulo esta com {temperatura} graus")
        elif 'fim' in query or 'sair' in query:
            print("sair")
            speak("Volte sempre!")
            break


        else:

            print("opção invalida")
            speak('não entendi o que você disse.')
            speak("Por favor, vamos tentar novamente. escolha uma opção válida.")