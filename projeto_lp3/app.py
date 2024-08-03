#importa a classe Flask do módulo flask
from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ

lista_produtos = [
        {"nome" : "Produto1", "descricao": "Descrição"},
        {"nome" : "Produto2", "descricao": "Descrição"},
        {"nome" : "Produto3", "descricao": "Descrição"}
    ]

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contato")
def contato():
    cpf = CPF()
    cnpj = CNPJ()
    return render_template("contato.html", cpf = cpf.generate(True), cnpj = cnpj.generate(True))


@app.route("/produtos")
def produtos():
    

    return render_template("produtos.html", produtos = lista_produtos)


@app.route("/serviços")
def servico():
    return "<h2>Nossos Serviços<h2>"

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

@app.route("/produtos", methods=['POST'])
def salvar_produtos():
    nome = request.form['nome']
    descricao = request.form['descricao']
    produto = {"nome": nome, "descricao": descricao}
    lista_produtos.append(produto)
    return render_template("produtos.html", produtos=lista_produtos)


@app.route("/termos-de-uso")
def termos():

    return render_template("termos.html")


@app.route("/politicas-de-privacidade")
def politicas():

    return render_template("politicas.html")


@app.route("/como-usar")
def comousar():

    return render_template("comousar.html")