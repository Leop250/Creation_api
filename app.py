

from flask import Flask, render_template, request

app = Flask(__name__)
books = [
{"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
{"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
{"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
{"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
{"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}]

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/api/v1/qui-suis-je/<name>', methods=["GET"])
def qui_suis_je(name):
    return name

@app.route('/somme/<int:a>/<int:b>', methods=["GET"])
def somme(a, b):
    return str(a + b)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    return f'recherche {query}'


@app.route('/searchbook', methods=['GET'])
def recherche_book():
    query = request.args.get('query', '').lower()
    for book in books:
        if query in book['title'].lower() or query in book['author'].lower():
            return f'{book}'
    return 'Aucun livre ne correspond à votre recherche.'
@app.route('/addbook', methods=['POST'])
def addbook():
    new_book = {}
    id = request.form.get('id')
    title = request.form.get('title')
    author = request.form.get('author')
    year = request.form.get('year')


    new_book['id'] = id
    new_book['title'] = title
    new_book['author'] = author
    new_book['year'] = year


    books.append(new_book)
    return f"Livre ajouté avec succès : {new_book}", 201

@app.route('/login', methods=['POST'])
def schearch_name():
    nom = request.form.get('username')
    return f'Nom : {nom}'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)