# -*- coding: utf-8 -*-
import sys
import funcoes

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
		funcoes.cadastrarPatrimonio()
	elif opc == 2:
		funcoes.cadastrarProfessor()
	elif opc == 3:
		funcoes.retirarPratimonio()
	elif opc == 4:
		funcoes.reporPratimonio()
	elif opc == 5:
		funcoes.pratimoniosAguardandoDevolucao()
	elif opc == 6:
		funcoes.pratimoniosDisponiveis()
	elif opc == 7:
		funcoes.listagemProfessores()
	elif opc == 8:
		funcoes.listagemPratimoniosMaisUsados()
	elif opc == 0:
		sys.exit()
	else:
		print("Digite Um valor Valido!")
		menu()


#funcoes.carregarAcessos()
#funcoes.carregarProfessor()
#funcoes.carregarPatrimonios()
#funcoes.cadastrarPatrimonio()
#funcoes.cadastrarProfessor()
menu()
