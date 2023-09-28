from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
id_set = set()

livros = [
    {
        'id': 1,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Câmara Secreta',
        'autor': 'J.K. Rowling'
    },
    {
        'id': 3,
        'título': 'Harry Potter e a Prisioneiro de Azkaban',
        'autor': 'J.K. Rowling'
    },
    {
        'id': 4,
        'título': 'Harry Potter e o Cálice de Fogo',
        'autor': 'J.K. Rowling'
    },
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify('Id não encontrado'), 400
        
@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    for livro in livros:
        if livro.get('id') == novo_livro.get('id'):
            return jsonify('id ja cadastrado'), 400
        if livro.get('autor') != novo_livro.get('autor'):
            return jsonify('Autor não aceito'), 400
    livros.append(novo_livro)
    response = make_response(jsonify(livros), 201)
    return response

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_editado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_editado)
            return jsonify(livros[indice])
        
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice , livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)
    return jsonify('Id não encontrado'), 400

app.run(port=5000, host='localhost', debug=True)
