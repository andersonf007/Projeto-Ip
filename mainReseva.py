# -*- coding: utf-8 -*-
import sys
from datetime import datetime
import os
#def restart_program():
#    python = sys.executable
#    os.execl(python, python, * sys.argv)

patrimonioLista = []
patrimonioDicionario = {}
professorLista = []
professorDicionario = {}
acessoLista = []
acessoDicionario = {}
patrimoniosAguardandoDevolucaoLista = []
patrimoniosAguardandoDevolucaoDicionatio = {}

#def patrimoniosAguardandoDevolucao

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
		dados[6] = dados[6].rstrip("\n")
		dados[6] = dados[6].lstrip(" ")
		acessoDicionario = {'matricula':dados[0],'patrimonio':dados[1],'tipoOp':dados[2],'dataR':dados[3],'horaR':dados[4],'dataD':dados[5],'horaD':dados[6]}
		acessoLista.append(acessoDicionario)
	db.close()

def cadastrarPatrimonio(id,disponibilidade):

	if id == 0:
		nome = input("Digite o nome do patrimonio:\n")
		numero = input("Digite o numero do patrimonio:\n")
		disponibilidade = 0 #onde a disponibilidade for zero o equipamento estará disponivel
		db = open('patrimonio.txt','a')
		db.write('{} / {} / {}\n'.format(nome,numero,disponibilidade))
		db.close()
		patrimonioDicionario = {'nome': nome,'numero': numero,'disponibilidade': disponibilidade}
		patrimonioLista.append(patrimonioDicionario)
		print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print("Patrimônio cadastrado com sucesso!")
		menu()
	else:	#nesse else ele vai alterar a disponibilidade do patrimonio reescrevendo as informacoes no arquivo
		db = open('patrimonio.txt','w')
		for j in patrimonioLista:
			if id == j['numero']:
				db.write('{} / {} / {}\n'.format(j['nome'],j['numero'],disponibilidade))
			else:
				db.write('{} / {} / {}\n'.format(j['nome'],j['numero'],j['disponibilidade']))
		db.close()
		if disponibilidade == 1 or  disponibilidade == '1':	#nesse if ele vai verificar se ele retirou ou repôs um patrimônio para poder apresentar a mensagem correta
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
			print("O patrimônio pode ser retirado!")
		elif disponibilidade == 0 or disponibilidade == '0':
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
			print("O patrimônio agora está disponivel para retirada!")
		menu()

def cadastrarProfessor():
	nome = input("Digite o nome do professor:\n")
	senha = input("Digite o senha do professor:\n")
	senha = criptografarSenha(senha)
	matricula = input("Digite o numero de matricula do professor:\n")
	db = open('professor.txt', 'a')
	db.write('{} / {} / {}\n'.format(nome,senha,matricula))
	db.close()
	professorDicionario = {'nome': nome,'senha': senha,'matricula':matricula}
	professorLista.append(professorDicionario)
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
	print("Professor cadastrado com sucesso!")
	menu()

def cadastrarAcesso(cadastrar,matricula,patrimonio,tipoOp,dataR,horaR,dataD,horaD):	#A dataD e horaD são os horarios da devolução do patrimonio
	if cadastrar == 0:
		db = open('acesso.txt', 'a')
		db.write('{} / {} / {} / {} / {} / {} / {}\n'.format(matricula,patrimonio,tipoOp,dataR,horaR,0,0))
		db.close()
		acessoDicionario = {'matricula':matricula,'patrimonio':patrimonio,'tipoOp':tipoOp,'dataR':dataR,'horaR':horaR}
		acessoLista.append(acessoDicionario)
	else:
		db = open('acesso.txt', 'w')
		for j in acessoLista:
			if j['matricula'] == matricula and j['patrimonio'] == patrimonio and j['tipoOp'] == 'retirada':
				db.write('{} / {} / {} / {} / {} / {} / {}\n'.format(j['matricula'],j['patrimonio'],tipoOp,j['dataR'],j['horaR'],dataD,horaD))
			else:
				db.write('{} / {} / {} / {} / {} / {} / {}\n'.format(j['matricula'],j['patrimonio'],j['tipoOp'],j['dataR'],j['horaR'],j['dataD'],j['horaD']))
		
def retirarPratimonio():
	matricula = input("Digite sua matricula:\n")
	senha = input("Digite sua senha:\n")
	senha = criptografarSenha(senha)
	for i in professorLista: # varre a lista de professores
		if matricula == i['matricula']: # confere se a matricula bate
			if senha == i['senha']:	# confere se a senha bate
				print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
				print("Seja bem vindo(a) prof. {}".format(i['nome']))
				print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
				patrimonio = input("Digite o numero do patrimonio:\n")
				for j in patrimonioLista:
					if patrimonio == j['numero']:	#confere se o patrimonio existe na lista
						if j['disponibilidade'] == 0 or j['disponibilidade'] == '0':	#verifica se o patrimonio esta disponivel
							j['disponibilidade'] = '1'	#altera a disponibilidade do patrimonio
							tipoOperacao = 'retirada'
							data = dataAtual()
							hora = horaAtual()
							cadastrarAcesso(0,matricula,patrimonio,tipoOperacao,data,hora,0,0)
							cadastrarPatrimonio(patrimonio,j['disponibilidade'])
							#restart_program()
							menu()
						else:
							print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
							print("Esse patrimonio não está disponivel")
							menu()
			else:
				print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
				print("Matricula ou senha incorretas")
				menu()

def reporPratimonio():
	matricula = input("Digite sua matricula:\n")
	senha = input("Digite sua senha:\n")
	senha = criptografarSenha(senha)
	for i in professorLista: # varre a lista de professores
		if matricula == i['matricula']: # confere se a matricula bate
			if senha == i['senha']:	# confere se a senha bate
				print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
				print("Seja bem vindo(a) prof. {}".format(i['nome']))
				print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
				patrimonio = input("Digite o numero do patrimonio:\n")
				for j in patrimonioLista:
					if patrimonio == j['numero']:	#confere se o patrimonio existe na lista
						if j['disponibilidade'] == 1 or j['disponibilidade'] == '1':	#verifica se o patrimonio esta em uso
							j['disponibilidade'] = '0'	#altera a disponibilidade do patrimonio
							tipoOperacao = 'devolução'
							data = dataAtual()
							hora = horaAtual()
							cadastrarAcesso(1,matricula,patrimonio,tipoOperacao,0,0,data,hora)
							cadastrarPatrimonio(patrimonio,j['disponibilidade'])
							#restart_program()
							menu()
						else:
							print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
							print("Esse patrimonio não foi retirado!")
							menu()
			else:
				print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
				print("Matricula ou senha incorretas")
				menu()

def menu():
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print("|                 Digite o número correspondente                 |")
	print("| 1 - Cadastrar o patrimônio                                     |")
	print("| 2 - Cadastrar o professor                                      |")
	print("| 3 - Retirar patrimônio                                         |")
	print("| 4 - Repor patrimônio                                           |")
	print("| 5 - Patrimonios aguardando devolução                           |")
	print("| 6 - Pratimonios disponiveis                                    |")
	print("| 7 - Listagem dos professores que ficaram com os patrimonios    |")
	print("| 8 - Listagem dos patrimônios mais utilizados                   |")
	print("| 0 - Sair                                                       |")
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

	opc = int(input())

	if opc == 1:
		cadastrarPatrimonio(0,0)
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


carregarAcessos()
carregarProfessor()
carregarPatrimonios()
#cadastrarPatrimonio(0)
#cadastrarProfessor()
menu()
