from flask import Flask, jsonify
from main import app, db
from models import Livro, Usuario

@app.route('/livro', methods =['GET'])
def get_livro():
    livros = Livro.query.all()
    livros_dic = []
    for livro in livros:
        livro_dic = {
            'id_livros': livro.id_livros,
            'titulo': livro.titulo,
            'autor': livro.autor,
            'ano_publicado': livro.ano_publicado
        }
        livros_dic.append(livro_dic)
    return jsonify(
        mensagem='Lista livros',
        livros=livros_dic
    )