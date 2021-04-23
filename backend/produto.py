#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


# Dados para acessa o banco
user = 'postgres'
password = '123456'
host = 'localhost'
db = 'estoque'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://"+user+":"+password+"@"+host+"/"+db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True

# Iniciar a conexão com o banco de Dados
db = SQLAlchemy(app)


class produtos(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    descricao = db.Column(db.String())
    unidadeMedida = db.Column(db.String())

    def __init__(self, name, descricao, unidadeMedida ):
        self.name = name
        self.descricao = descricao
        self.unidadeMedida = unidadeMedida

CORS(app)


@app.route("/produto", methods=["GET", "POST"])
def getProduto():
    if request.method == 'GET':
    
        product = produtos.query.order_by(produtos.id).all()
        output = []
        for produto in product:
            listProduto = {}
            listProduto["id"] = produto.id
            listProduto["name"] = produto.name
            listProduto["descricao"] = produto.descricao
            listProduto["unidadeMedida"] = produto.unidadeMedida
            output.append(listProduto)
        return jsonify(output)

    elif request.method == 'POST':
        dadosProduto = request.get_json()
        insertProduto = produtos(name=dadosProduto['name'], descricao=dadosProduto['descricao'], unidadeMedida=dadosProduto['unidadeMedida'])
        db.session.add(insertProduto)
        db.session.commit()
        return "Cadastrado com Sucesso"


@app.route("/produto/<id_>", methods=["PUT", "DELETE"])
def atualizarProduto(id_):
    product = produtos.query.filter_by(id=id_).first()
    if request.method == 'PUT':
        dadosProduto = request.get_json()
        product.name = dadosProduto['name']
        product.descricao = dadosProduto['descricao']
        product.unidadeMedida = dadosProduto['unidadeMedida']
        db.session.commit()
        return "Atualizado com Sucesso"

    if request.method == 'DELETE':
        db.session.delete(product)
        db.session.commit()
        return "Deletado com Sucesso"


# migration
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


if __name__ == '__main__':
    app.run()


