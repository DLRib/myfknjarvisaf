import pyttsx3

engine = pyttsx3.init('sapi5')

# configurar a voz
voice = engine.getProperty('voices')
engine.setProperty("voice", voice[0].id)
engine.setProperty('rate', 300)
engine.setProperty('pitch', 0.2)

# função para agilizar as falas, só usar "speak('fala')"
def speak(tts):
    engine.say(tts)
    engine.runAndWait()

def comandos(ordem):
    if 'tudo bem' in ordem:
        speak ('bem, e você?')
    elif 'oi' in ordem:
        speak('Olá, tudo bem?')
    elif 'desligar' in ordem:
        return 1
    


'Olá, Senhor'
'Bom dia, Senhor'
'Boa tarde, Senhor'
'Boa noite, senhor'
'como se sente hoje?'
'gostaria de ouvir uma música?'
'iremos descansar hoje?, ou nós vamos trabalhar?'
'o dia está ensolarado, perfeito para []'
'gostaria de sugestões sobre []?'
'gostaria de sugestões para me melhorar?'
'o que o senhor gostaria de fazer hoje?'
# momentos de "tédio"
 
'gostaria de fazer seu Daily Tracker agora?'
'o Senhor deseja jogar algum jogo? posso ligar seu ps4 para o senhor relaxar'
'qual playlist devo escolher para melhorar o seu dia?'
'podemos fazer uma nova lista de comandos e situações para meu treinamento'

# lembretes

'devo lembrar que seu Treino de Boxe começa as 18:30, faltam [] minutos'
'devo lembrar de algo para o senhor mais tarde?'
'eu gostaria de listar os seus compromissos do dia'
'lembrarei disso'
'[] quantas vezes?'
'gostaria de adicionar em eventos recorrentes?'
'a que horas devo te acordar?'

# modos

'modo família'
'modo alerta'
'modo silencioso'
'modo auxiliar/ajudante/companheiro/copiloto'

# módulos

'iniciando módulo homem-aranha, é um prazer trabalhar nesse projeto novamente'
'iniciando módulo vigia'
'iniciando módulo 7, tenha um ótima noite, senhor'

# saudações

'sempre um prazer ter o Senhor de volta'
'Olá, Senhor'



# ele deve observar meu estado e emoção, então começar a conversar