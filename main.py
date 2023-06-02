import pyaudio
import vosk
import pyttsx3_conf
import json
from textblob import TextBlob



def analisar_sentimento(texto):
    blob = TextBlob(texto)
    blob = blob.translate(to='en')
    polaridade = blob.sentiment.polarity

    if polaridade > 0:
        return "Sentimento positivo"
    elif polaridade < 0:
        return "Sentimento negativo"
    else:
        return "Sentimento neutro"


# Configurações do PyAudio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 32000
CHUNK = 1024

# Inicializa o PyAudio, e o Vosk
pa = pyaudio.PyAudio()
model = vosk.Model("model")

# criar um objeto Vosk Recognizer
rec = vosk.KaldiRecognizer(model, RATE)

# começar a gravar (iniciar a gravação)
stream = pa.open(format=FORMAT,
                 channels=CHANNELS,
                 rate=RATE,
                 input=True,
                 frames_per_buffer=CHUNK)

desligar = 0
print('Estou te ouvindo...') 

# Reconhcendo/Gravando em si
while desligar != 1:

    # Lê os dados do "stream" do áudio que está sendo captado
    data = stream.read(CHUNK)

    # Enviar os dados que acabaram de ser captados para o VOSK hehe
    if rec.AcceptWaveform(data):# "se" ele reconhecer algo...

        # escreva qual o resultado, o que reconheceu.
        result = rec.Result()
        result = json.loads(result)
        result = result['text']
        print('Primeiro resultado: ', result)
        desligar = pyttsx3_conf.comandos(result)
        sentimento = analisar_sentimento(result)
        print(sentimento)
        

            

# Encerrar
stream.stop_stream()
stream.close()
pa.terminate()