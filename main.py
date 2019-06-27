import sys
patrimonio = []
professor = []
acesso = []

def carregarPatrimonios():

	db = open('patrimonio','r')
	for entrada in db:
		dados = entrada.split("/")
		patrimonio.apeend({'nome': dados[0],'numero': dados[1],'disponibilidade': dados[2]})
	db.close()

	print(patrimonio)
def carregarProfessor():

	db = open('professor','r')
	for entrada in db:
		dados = entrada.split("/")
		professor.apeend({dados[0],dados[1],dados[2]})
	db.close()

def carregarAcessos():

	db = open('acesso','r')
	for entrada in db:
		dados = entrada.split("/")
		acesso.apeend({dados[0],dados[1],dados[2],dados[3],dados[4],dados[5]})
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
#carregarProfessor()
carregarPatrimonios()
#cadastrarPatrimonio()
#cadastrarProfessor()
menu()
