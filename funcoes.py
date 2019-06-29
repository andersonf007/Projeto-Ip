# -*- coding: utf-8 -*-
import sys
import main
from datetime import datetime

patrimonioLista = []
patrimonioDicionario = {}
professorLista = []
professorDicionario = {}
acessoLista = []
acessoDicionario = {}

def horaAtual():
	horarioatual = datetime.now()
	horaFormatada = "{}:{}:{}".format(horarioatual.hour, horarioatual.minute,horarioatual.second)
	return horaFormatada

def dataAtual():
	dataAtual = datetime.today()
	dataFormatada = "{} de {} de {}".format(dataAtual.day, dataAtual.month,dataAtual.year)
	return dataFormatada

def criptografarSenha(senha):
    senhaCriptografada = ''
    for i in senha:
        senhaCriptografada += chr(ord(i) + 30)
    return senhaCriptografada

def carregarPatrimonios():
	patrimonio = []
	db = open('patrimonio.txt','r')
	for entrada in db:
		dados = entrada.split("/")
		dados[2] = dados[2].rstrip("\n")
		dados[2] = dados[2].lstrip(" ")
		patrimonioDicionario = {'nome': dados[0],'numero': dados[1],'disponibilidade': dados[2]}
		patrimonioLista.append(patrimonioDicionario)
	db.close()

def carregarProfessor():

	db = open('professor.txt','r')
	for entrada in db:
		dados = entrada.split("/")
		dados[1] = dados[1].strip(" ")
		dados[2] = dados[2].rstrip("\n")
		dados[2] = dados[2].lstrip(" ")
		professorDicionario = {'nome': dados[0],'senha': dados[1],'matricula':dados[2]}
		professorLista.append(professorDicionario)
	db.close()

def carregarAcessos():

	db = open('acesso.txt','r')
	for entrada in db:
		dados = entrada.split("/")
		dados[4] = dados[4].rstrip("\n")
		dados[4] = dados[4].lstrip(" ")
		acessoDicionario = {'matricula':dados[0],'patrimonio':dados[1],'tipoOp':dados[2],'data':dados[3],'hora':dados[4]}
		acessoLista.append(acessoDicionario)
	db.close()

def cadastrarPatrimonio():

	nome = input("Digite o nome do patrimonio:\n")
	numero = input("Digite o numero do patrimonio:\n")
	disponibilidade = 0 #onde a disponibilidade for zero o equipamento estará disponivel

	db = open('patrimonio.txt','a')
	db.write('{} / {} / {}\n'.format(nome,numero,disponibilidade))
	db.close()
	carregarPatrimonios()
	main.menu()

def cadastrarProfessor():
	nome = input("Digite o nome do professor:\n")
	senha = input("Digite o senha do professor:\n")
	senha = criptografarSenha(senha)
	matricula = input("Digite o numero de matricula do professor:\n")

	db = open('professor.txt', 'a')
	db.write('{} / {} / {}\n'.format(nome,senha,matricula))
	db.close()
	#carregarProfessor()
	main.menu()

def cadastrarAcesso(matricula,patrimonio,tipoOp,data,hora):
    db = open('acesso.txt', 'a')
	db.write('{} / {} / {} / {} / {}\n'.format(matricula,patrimonio,tipoOp,data,hora))
	db.close()
	main.menu()

def retirarPratimonio():
	matricula = input("Digite sua matricula:\n")
	senha = input("Digite sua senha:\n")
	senha = criptografarSenha(senha)
	for i in professorLista:
		if matricula == i['matricula']:
			if senha == i['senha']:
				patrimonio = input("digite o numero do patrimonio")
				tipoOperacao = 'retirada'
				data = dataAtual()
				hora = horaAtual()
				cadastrarAcesso(matricula,patrimonio,tipoOperacao,data,hora)
			else:
				print("Matricula ou senha incorretas")
