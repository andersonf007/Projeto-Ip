# -*- coding: utf-8 -*-
import sys
from datetime import *
import os

patrimonioLista = []
patrimonioDicionario = {}
professorLista = []
professorDicionario = {}
acessoLista = []
acessoDicionario = {}
patrimoniosAguardandoDevolucaoLista = []
patrimoniosAguardandoDevolucaoDicionatio = {}

#Recebe uma string separa ela em partes específicas para converter em datetime
def converterStringDatetime(variavel):
	if variavel != ' 0':
		dados = variavel.split("-")
		dados2 = variavel.split(":")
		ano = int(dados[0])
		mes = int(dados[1])
		dia = int(dados[2].split(' ')[0])
		hora = int(dados2[0].split(' ')[2])
		minutos = int(dados2[1])
		return datetime(year=ano,month=mes,day=dia,hour=hora,minute=minutos)
	else:
		return variavel

def listagemProfessores():
	lista = []
	lista2 = []
	dicionario = {}
	patrimonio = input("Digite o numero do patrimônio:\n")
	horas = int(input("Por mais de quantas horas?\n"))
	dias = int(input("Nos últimos quantos dias?\n"))
	for i in acessoLista:
		if i['tipoOp'] == 'devolucao' and i['patrimonio'] == patrimonio: #Compara as informações digitadas com as informações na lista de acesso
			data = datetime.today() - timedelta(days=dias,hours=horas) #subtrai a data e a hora
			if i['dataR'] >= data:	#Verifica as datas informada é inferior as datas no arquivo
				for j in professorLista:
					if j['matricula'] == i['matricula']:
						dicionario = {'nome':j['nome'],'matricula':j['matricula']}
						lista.append(dicionario)	#Essa lista esta com informaçõesem duplicidade

	for k in lista: # varre a lista que esta com duplicidade e confere com a lista2 que nao tem duplicidade!
		if k['nome'] not in lista2:
			lista2.append(k['nome'])
			print("Professor: {} / Matricula: {} ".format(k['nome'],k['matricula']))

def listagemPratimoniosMaisUsados():
	lista = []
	cont = 0
	dias = int(input("Nos últimos quantos dias?\n"))
	for i in acessoLista:
		data = datetime.today() - timedelta(days=dias)
		if i['dataR'] >= data:
			lista.append(i['patrimonio']) 	#Nessa lista so tem os codigos dos patrimônios na qual teve movimentação

	for j in patrimonioLista:
		for i in lista:
			if i == j['numero']:	#compara as informações da lista junto com a lista de patrimonio para realizar a contagem e poder mostrar os nomes dos Patrimônios
				cont += 1
		print("Patrimônio - {} Foi utilizado {} vezes".format(j['nome'],cont))
		cont = 0
	menu()

def patrimoniosAguardandoDevolucao():
	for i in acessoLista:
		if i['tipoOp'] == 'retirada':
			print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
			print("Nª do patrimonio: {}".format(i['patrimonio']))
			print("Retirado no dia: {}".format(i['dataR']))
	menu()

def pratimoniosDisponiveis():
	for i in patrimonioLista:
		if i['disponibilidade'] == '0' or i['disponibilidade'] == 0:
			print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
			print("Nome do patrimonio: {}".format(i['nome']))
			print("Nª do patrimonio: {}".format(i['numero']))
	menu()

def dataAtual():
	dataAtual = datetime.today()
	return dataAtual

#O metodo ord() retorna um inteiro referente ao caracter na tabela ascii que é somado 25 e vai para chr() que recebe um interiro e retorna uma string de acordo com o unicode
def criptografarSenha(senha):
	criptografada = ''
	for c in senha:
		criptografada += chr(ord(c)+25)
	return criptografada

#Recebe as informações que está no arquivo txt, realiza alguns passos para melhorar a manipulação e insere no final na lista
def carregarPatrimonios():

	db = open('patrimonio.txt','r')
	for entrada in db:
		if entrada != '\n':
			dados = entrada.split("#")
			dados[1] = dados[1].strip(" ")
			dados[2] = dados[2].rstrip("\n")
			dados[2] = dados[2].lstrip(" ")
			patrimonioDicionario = {'nome': dados[0],'numero': dados[1],'disponibilidade': dados[2]}
			patrimonioLista.append(patrimonioDicionario)
		else:
			print("Não à dados de patrimonio no sistema no sistema!")
	db.close()

#Recebe as informações que está no arquivo txt, realiza alguns passos para melhorar a manipulação e insere no final na lista
def carregarProfessor():

	db = open('professor.txt','r')
	for entrada in db:
		if entrada != '\n':
			dados = entrada.split("#")
			dados[1] = dados[1].strip(" ")
			dados[2] = dados[2].rstrip("\n")
			dados[2] = dados[2].lstrip(" ")
			professorDicionario = {'nome': dados[0],'senha': dados[1],'matricula':dados[2]}
			professorLista.append(professorDicionario)
		else:
			print("Não à dados de professores no sistema no sistema!")
	db.close()

#Recebe as informações que está no arquivo txt, realiza alguns passos para melhorar a manipulação e insere no final na lista
def carregarAcessos():

	db = open('acesso.txt','r')
	for entrada in db:
		if entrada != '\n':
			dados = entrada.split("#")
			dados[0] = dados[0].strip(" ")
			dados[1] = dados[1].strip(" ")
			dados[2] = dados[2].strip(" ")
			dados[4] = dados[4].rstrip("\n")
			dataR = converterStringDatetime(dados[3])
			dataD = converterStringDatetime(dados[4])
			acessoDicionario = {'matricula':dados[0],'patrimonio':dados[1],'tipoOp':dados[2],'dataR':dataR,'dataD':dataD}
			acessoLista.append(acessoDicionario)
		else:
			print("Não à dados de movimentação de patrimonio no sistema no sistema!")
	db.close()

def cadastrarPatrimonio(id,disponibilidade):

	if id == 0:	#realiza o cadastro as informações no arquivo utilizando o append
		nome = input("Digite o nome do patrimonio:\n")
		numero = input("Digite o numero do patrimonio:\n")
		disponibilidade = 0 #onde a disponibilidade for zero o equipamento estará disponivel
		retorno = next((p for p in patrimonioLista if p['numero'] == numero), None)
		if retorno != None:
			print("Patrimônio ja encontra-se cadastrado!")
		else:
			db = open('patrimonio.txt','a')
			db.write('{} # {} # {}\n'.format(nome,numero,disponibilidade))
			db.close()
			patrimonioDicionario = {'nome': nome,'numero': numero,'disponibilidade': disponibilidade}
			patrimonioLista.append(patrimonioDicionario)
			print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
			print("Patrimônio cadastrado com sucesso!")
	else:	#nesse else ele vai alterar a disponibilidade do patrimonio reescrevendo as informacoes no arquivo
		db = open('patrimonio.txt','w')
		for j in patrimonioLista:
			if id == j['numero']:
				db.write('{} # {} # {}\n'.format(j['nome'],j['numero'],disponibilidade))
			else:
				db.write('{} # {} # {}\n'.format(j['nome'],j['numero'],j['disponibilidade']))
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
	db.write('{} # {} # {}\n'.format(nome,senha,matricula))
	db.close()
	professorDicionario = {'nome': nome,'senha': senha,'matricula':matricula}
	professorLista.append(professorDicionario)
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
	print("Professor cadastrado com sucesso!")
	menu()

def cadastrarAcesso(cadastrar,matricula,patrimonio,tipoOp,dataR,dataD):	#A dataD e horaD são os horarios da devolução do patrimonio
	if cadastrar == 0:	#Realiza o cadastro das informações no arquivo de acesso
		dataDevolucao = 0
		db = open('acesso.txt', 'a')
		db.write('{} # {} # {} # {} # {}\n'.format(matricula,patrimonio,tipoOp,dataR,dataDevolucao))
		db.close()
		acessoDicionario = {'matricula':matricula,'patrimonio':patrimonio,'tipoOp':tipoOp,'dataR':dataR,'dataD':dataDevolucao}
		acessoLista.append(acessoDicionario)
	else:	#reescreve todas as informações do arquivo acesso para poder alterar o tipo de operação e a data de devolução do patrimômio
		db = open('acesso.txt','w')
		for j in acessoLista:
			if j['matricula'] == matricula and j['patrimonio'] == patrimonio and j['tipoOp'] == 'retirada':
				db.write('{} # {} # {} # {} # {}\n'.format(j['matricula'],j['patrimonio'],tipoOp,j['dataR'],dataD))
			else:
				db.write('{} # {} # {} # {} # {}\n'.format(j['matricula'],j['patrimonio'],j['tipoOp'],j['dataR'],j['dataD']))
		db.close()

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
							cadastrarAcesso(0,matricula,patrimonio,tipoOperacao,data,0)
							cadastrarPatrimonio(patrimonio,j['disponibilidade'])
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
							for k in acessoLista:
								if k['matricula'] == matricula and k['patrimonio'] == patrimonio and k['tipoOp'] == 'retirada':
									k['tipoOp'] = 'devolucao'	#altera o tipo de operação do acesso
									j['disponibilidade'] = '0'	#altera a disponibilidade do patrimonio
									data = dataAtual()
									k['dataD'] = data	#recebe a data atual para saber a hora que o professor esta devolvendo o patrimômio
									cadastrarAcesso(1,matricula,patrimonio,'devolucao',0,data)
									cadastrarPatrimonio(patrimonio,j['disponibilidade'])
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
		patrimoniosAguardandoDevolucao()
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
menu()
