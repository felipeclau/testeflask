from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template ("index.html")



@app.route('/detalhesEletronica')
def eletronica():
    return render_template('detalhesEletronica.html')


@app.route('/detalhesInformaticaIndustrial')
def informaticaIndustrial():
    return render_template('detalhesInformáticaIndustrial.html')

@app.route('/detalhesMecatronica')
def mecatronica():
    return render_template('detalhesMecatronica.html')



@app.route('/detalhesTelecomunicacoes')
def telecomunicacoes():
    return render_template('detalhesTelecomunicacoes.html')



@app.route('/matrizCurricular_Eletronica')
def matrizEletronica():
    return render_template('matrizCurricular_Eletronica.html')


@app.route('/matrizCurricular_InformaticaIndustrial')
def matrizInformaticaIndustrial():
    return render_template('matrizCurricular_InformaticaIndustrial.html')



@app.route('/matrizCurricular_Mecatronica')
def matrizMecatronica():
    return render_template('matrizCurricular_Mecatronica.html')


@app.route('/matrizCurricular_Telecomunicacoes')
def matrizTelecomunicacoes():
    return render_template('matrizCurricular_Telecominucacoes.html')



@app.route('/listaCurso.html')
def listacurso():
    return render_template ("listaCurso.html")

@app.route('/noticias.html')
def noticias():
    return render_template("noticias.html")

app.run()
