import speech_recognition as sr

# Função para reconhecer e executar comandos
def reconhecer_comandos(entrada):
    if "olá" in entrada:
        print("Olá! Como posso ajudar?")
    elif "tempo" in entrada:
        print("O tempo está ensolarado hoje.")
    elif "tchau" in entrada:
        print("Até logo!")
        exit()
    else:
        print("Desculpe, não entendi o comando.")

# Inicializar o reconhecedor de voz
r = sr.Recognizer()

while True:
    try:
        # Capturar áudio do microfone
        with sr.Microphone() as source:
            print("Diga algo...")
            audio = r.listen(source)

        # Reconhecer o áudio usando o Google Speech Recognition
        entrada = r.recognize_google(audio, language="pt-BR")

        # Exibir o texto reconhecido
        print("Você disse:", entrada)

        # Chamar a função para reconhecer e executar comandos
        reconhecer_comandos(entrada)

    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print("Erro ao recuperar resultados do serviço de reconhecimento de voz:", e)