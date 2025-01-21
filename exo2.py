
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def schearch_name():
    nom = request.form.get('username')
    motdepasse = request.form.get('mostsdepasse')
    return f'Nom : {nom} Password: {motdepasse}'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)