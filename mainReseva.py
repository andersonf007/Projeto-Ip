# -*- coding: utf-8 -*-
import sys
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
    for caracter in senha:
        senhaCriptografada += chr(ord(caracter) + 10)
    return senhaCriptografada

def carregarPatrimonios():

	db = open('patrimonio.txt','r')
	for entrada in db:
		dados = entrada.split("/")
		dados[1] = dados[1].strip(" ")
		dados[2] = dados[2].rstrip("\n")
		dados[2] = dados[2].lstrip(" ")
		patrimonioDicionario = {'nome': dados[0],'numero': dados[1],'disponibilidade': dados[2]}
		patrimonioLista.append(patrimonioDicionario)
	db.close()
	#print(patrimonioLista)

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

def cadastrarPatrimonio(id):

	if id == 0:
		nome = input("Digite o nome do patrimonio:\n")
		numero = input("Digite o numero do patrimonio:\n")
		disponibilidade = 0 #onde a disponibilidade for zero o equipamento estará disponivel
		db = open('patrimonio.txt','a')
		db.write('{} / {} / {}\n'.format(nome,numero,disponibilidade))
		db.close()
		menu()
	else:
		db = open('patrimonio.txt','w')
		for j in patrimonioLista:
			if id == j['numero']:
				j['disponibilidade'] = 1
				db.write('{} / {} / {}\n'.format(j['nome'],j['numero'],j['disponibilidade']))
			else:
				db.write('{} / {} / {}\n'.format(j['nome'],j['numero'],j['disponibilidade']))
		db.close()
		menu()

def cadastrarProfessor():
	nome = input("Digite o nome do professor:\n")
	senha = input("Digite o senha do professor:\n")
	senha = criptografarSenha(senha)
	matricula = input("Digite o numero de matricula do professor:\n")

	db = open('professor.txt', 'a')
	db.write('{} / {} / {}\n'.format(nome,senha,matricula))
	db.close()
	#carregarProfessor()
	menu()

def cadastrarAcesso(matricula,patrimonio,tipoOp,data,hora):
	db = open('acesso.txt', 'a')
	db.write('{} / {} / {} / {} / {}\n'.format(matricula,patrimonio,tipoOp,data,hora))
	db.close()

def retirarPratimonio():
	matricula = input("Digite sua matricula:\n")
	senha = input("Digite sua senha:\n")
	senha = criptografarSenha(senha)
	for i in professorLista: # varre a lista de professores
		if matricula == i['matricula']: # confere se a matricula bate
			if senha == i['senha']:	# confere se a senha bate
				patrimonio = input("Digite o numero do patrimonio:\n")
				for j in patrimonioLista:
					print(j)
					if patrimonio == j['numero']:	#confere se o patrimonio existe na lista
						if j['disponibilidade'] == '0':	#verifica se o patrimonio esta disponivel
							j['disponibilidade'] = 1	#altera a disponibilidade do patrimonio
							tipoOperacao = 'retirada'
							data = dataAtual()
							hora = horaAtual()
							cadastrarAcesso(matricula,patrimonio,tipoOperacao,data,hora)
							cadastrarPatrimonio(patrimonio)
							menu()
						else:
							print("Esse patrimonio não está disponivel")
							menu()
			else:
				print("Matricula ou senha incorretas")
				menu()



def menu():
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print("|                 Digite o numero correspondente                 |")
	print("| 1 - Cadastrar o patrimônio                                     |")
	print("| 2 - Cadastrar o professor                                      |")
	print("| 3 - Retirar pratimonio                                         |")
	print("| 4 - Repor patrimonio                                           |")
	print("| 5 - Patrimonios aguardando devoicao                            |")
	print("| 6 - Pratimonios disponiveis                                    |")
	print("| 7 - Listagem dos professores que ficaram com os patrimonios    |")
	print("| 8 - Listagem dos pratimonios mais utilizados                   |")
	print("| 0 - Sair                                                       |")
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

	opc = int(input())

	if opc == 1:
		cadastrarPatrimonio(0)
	elif opc == 2:
		cadastrarProfessor()
	elif opc == 3:
		retirarPratimonio()
	elif opc == 4:
		reporPratimonio()
	elif opc == 5:
		pratimoniosAguardandoDevolucao()
	elif opc == 6:
		pratimoniosDisponiveis()
	elif opc == 7:
		listagemProfessores()
	elif opc == 8:
		listagemPratimoniosMaisUsados()
	elif opc == 0:
		sys.exit()
	else:
		print("Digite Um valor Valido!")
		menu()


#carregarAcessos()
carregarProfessor()
carregarPatrimonios()
#cadastrarPatrimonio(0)
#cadastrarProfessor()
menu()
