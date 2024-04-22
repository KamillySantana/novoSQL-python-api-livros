from main import db
class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100))
    senha = db.Column(db.String(254))
class Livro(db.Model):
    id_livros = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100))
    autor = db.Column(db.String(254))
    ano_publicado = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
