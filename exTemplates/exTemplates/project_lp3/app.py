from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ



app = Flask("My App")

@app.route("/")
def gerarCPF_home():
    cpf = CPF()

    return render_template("gerar-cpf.html", cpfs = cpf.generate(False))


@app.route("/gerar-cpf")
def gerarCPF():
    cpf = CPF()

    return render_template("gerar-cpf.html", cpfs = cpf.generate(False))


@app.route("/gerar-cnpj")
def gerarCNPJ():
    cnpj = CNPJ()

    return render_template("gerar-cnpj.html", cnpjs = cnpj.generate(False))


app.run()