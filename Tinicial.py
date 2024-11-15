import json 
from Funções import limpar_tela,adcionar_livro ,deletar_livro,listar_livro,listar_Autores,realizar_emprestimo,listar_livros_disponiveis,retirar_emprestimo, buscar_livro
import os


arquivo_json = 'User.json'
def carregar_dados():
    if os.path.exists(arquivo_json):
        with open(arquivo_json, 'r') as arquivo:
            return json.load(arquivo)
    else:
        return {"Livros": [], "Autores": [],"Lista de Livros": [],"Lista de Autores": [],"Emprestimos": []}

while True:
    limpar_tela()
    print("-"*5,"Bem vindo a Biblioteca Virtual", "-"*5)
    escolha = input("Escolha uma das opções abaixo:\n 1-Livros\n 2-Infomação dos Autores\n 3-Emprestimos\n 4-Sair do programa!\n")
    
    if not escolha.isdigit():
        print('Digite um valor Valido!')
        limpar_tela()
        continue

    escolha = int(escolha)

    if escolha == 1:
        limpar_tela()
        while True:
            print("-"*5,"Livros", "-"*5)
            resp = input('Digite uma das opções:\n1-Adcionar livro\n2-Listar livros\n3-Excluir Livro\n4-Sair\n')
            if not resp.isdigit():
                limpar_tela()
                print('Digite um valor Valido!')
                continue
            resp = int(resp)
            if resp == 1:
                limpar_tela()
                adcionar_livro()
            elif resp == 2:
                limpar_tela()
                listar_livro()
            elif resp == 3:
                limpar_tela()
                deletar_livro()
            else:
                break
    elif escolha ==2:
        limpar_tela()
        while True:
            print("-"*5,"Informações dos Autores", "-"*5)
            resp = input('Digite uma das opções:\n1-Listar Autores\n2-Sair\n')
            if not resp.isdigit():
                limpar_tela()
                print('Digite um valor Valido!')
                continue
            resp = int(resp)
            if resp == 1:
                limpar_tela()
                listar_Autores()
            else:
                break
    elif escolha == 3:
        limpar_tela()
        while True:
            print("-"*5,"Emprestimos", "-"*5)
            resp = input('Digite uma das opções:\n1-Emprestimo de livro\n2-Livros disponiveis para emprestimo\n3-Livros emprestados\n4-Buscar livro\n5-Sair\n')
            if not resp.isdigit():
                limpar_tela()
                print('Digite um valor Valido!')
                continue
            resp = int(resp)
            if resp == 1:
                limpar_tela()
                print("Selecione o livro:\n")
                realizar_emprestimo()
            elif resp == 2:
                limpar_tela()
                listar_livros_disponiveis()
            elif resp == 3:
                limpar_tela()
                retirar_emprestimo()
            elif resp == 4:
                limpar_tela()
                buscar_livro()
            else:
                break
    else:
        break