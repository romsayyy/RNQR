from flask import Flask, render_template

app = Flask(__name__)

# Variable pour suivre le nombre d'utilisateurs
nombre_de_personnes = 0

@app.route('/')
def index():
    return render_template('index.html', numero=nombre_de_personnes)

@app.route('/qr-scanned')
def qr_scanned():
    global nombre_de_personnes
    nombre_de_personnes += 1
    return render_template('index.html', numero=nombre_de_personnes)

if __name__ == '__main__':
    app.run(debug=True, host='10.0.220.130')
