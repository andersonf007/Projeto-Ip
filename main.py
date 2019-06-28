import sys
patrimonio = {}
professor = []
acesso = {}
#data = date.today()
def carregarPatrimonios():
	patrimonio = []
	db = open('patrimonio.txt','r')
	for entrada in db:
		dados = entrada.split("/")
		patrimonio.append([{'nome': dados[0],'numero': dados[1],'disponibilidade': dados[2]}])
	db.close()

def carregarProfessor():
	#professor = []
	db = open('professor.txt','r')
	for entrada in db:
		print(entrada)
		dados = entrada.split("/")
		#print(dados[0])
		#print(dados[1])
		dados[2] = dados[2].rstrip("\n")
		dados[2] = dados[2].lstrip(" ")
		#print(type(dados[2]))
		professor[0] = dados[0]
		professor[1] = dados[1]
		professor[2] = dados[2]

	db.close()

	print(professor)

def carregarAcessos():

	db = open('acesso.txt','r')
	for entrada in db:
		dados = entrada.split("/")
		acesso.append({dados[0],dados[1],dados[2],dados[3],dados[4],dados[5]})
	db.close()

def cadastrarPatrimonio():

	nome = input("Digite o nome do patrimonio:\n")
	numero = input("Digite o numero do patrimonio:\n")
	disponibilidade = 0 #onde a disponibilidade for zero o equipamento estará disponivel

	db = open('patrimonio.txt','a')
	db.write('{} / {} / {}\n'.format(nome,numero,disponibilidade))
	db.close()
	carregarPatrimonios()
	menu()

def cadastrarProfessor():
	nome = input("Digite o nome do professor:\n")
	senha = input("Digite o senha do professor:\n")
	matricula = input("Digite o numero de matricula do professor:\n")

	db = open('professor.txt', 'a')
	db.write('{} / {} / {}\n'.format(nome,senha,matricula))
	db.close()
	#carregarProfessor()
	menu()

def retirarPratimonio():
	matricula = input("Digite sua matricula:\n")
	senha = input("Digite sua senha:\n")
	for i in professor:
		print(i)
		print(type(i))
		if matricula == i['matricula']:
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
