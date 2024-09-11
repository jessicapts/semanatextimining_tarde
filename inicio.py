from gtts import gTTS
from flask import Flask,render_template,request
import os
#criando um objeto flask
app = Flask(__name__)

# / - Página principal . Post - recuperar
@app.route('/',methods=['GET', 'POST'])
def index():
    audio_path = None
    if request.method == 'POST':

            #Pegar valor do HTML <texfield>
            texto = request.form['texto']

            #Configurar o idioma
            lingua = 'pt-br'

            #criação do objeto
            tts = gTTS(text=texto,lang=lingua)

            #nome do arquivo de áudio
            audio_path = "static/audio_exemplo.mp3"

            #SaLvar o arquivo
            tts.save(audio_path)
        
    return render_template('index.html',audio_path=audio_path)

if __name__ == '__main__':
    app.run(debug=True)