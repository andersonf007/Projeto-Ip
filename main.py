import sys
patrimonio = []
professor = []
acesso = []
#data = date.today()
def carregarPatrimonios():
	patrimonio = []
	db = open('patrimonio','r')
	for entrada in db:
		dados = entrada.split("/")
		patrimonio.append([{'nome': dados[0],'numero': dados[1],'disponibilidade': dados[2]}])
	db.close()

def carregarProfessor():
	professor = []
	db = open('professor','r')
	for entrada in db:
		dados = entrada.split("/")
		#print(dados[0])
		dados[2] = dados[2].rstrip("\n")
		dados[2] = dados[2].lstrip(" ")
		print(type(dados[2]))
		professor.append([{'nome': dados[0], 'senha': dados[1],'matricula': dados[2]}])
	db.close()

	print(professor)

def carregarAcessos():

	db = open('acesso','r')
	for entrada in db:
		dados = entrada.split("/")
		acesso.append({dados[0],dados[1],dados[2],dados[3],dados[4],dados[5]})
	db.close()

def cadastrarPatrimonio():

	nome = input("Digite o nome do patrimonio:\n")
	numero = input("Digite o numero do patrimonio:\n")
	disponibilidade = 0 #onde a disponibilidade for zero o equipamento estará disponivel

	db = open('patrimonio','a')
	db.write('{} / {} / {}\n'.format(nome,numero,disponibilidade))
	db.close()
	menu()

def cadastrarProfessor():
	nome = input("Digite o nome do professor:\n")
	senha = input("Digite o senha do professor:\n")
	matricula = input("Digite o numero de matricula do professor:\n")

	db = open('professor', 'a')
	db.write('{} / {} / {}\n'.format(nome,senha,matricula))
	db.close()
	menu()
	#carregarProfessor()

def retirarPratimonio():
	matricula = input("Digite sua matricula:\n")
	senha = input("Digite sua senha:\n")

	for indice in professor:
		print(indice)
		print(type(indice))
		if matricula == indice[2]:
			print("oi")


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
		cadastrarPatrimonio()
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
#carregarPatrimonios()
#cadastrarPatrimonio()
#cadastrarProfessor()
menu()