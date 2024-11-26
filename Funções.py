import os
import json
from datetime import datetime

data = datetime.now().strftime("Data:%d/%m/%Y")


arquivo_json = 'User.json'
def carregar_dados():
    if os.path.exists(arquivo_json):
        with open(arquivo_json, 'r') as arquivo:
            return json.load(arquivo)
    else:
        return {"Livros": [], "Autores": [],"Emprestimos": []}
dados = carregar_dados()

def salvar_dados(dados):
    with open(arquivo_json, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def alunos():
    nome = input("Digite o nome de usuario!\n").lower()
    datanascimento = input("Informe da Data de Nascimento:\n")
    email = input("Informe o Email do usuario:\n").lower()
    aluno = {
        "id": gerar_novo_id(dados), 
        "nome": nome, 
        "dataNascimento":datanascimento, 
        "email":email
    }
    dados["Alunos"].append(aluno)
    salvar_dados(dados)
    limpar_tela()
    return

def gerar_novo_id(dados):
    if dados["Livros"]:
        ultimo_id = dados["Livros"][-1]["id"]
        return ultimo_id + 1
    else:
        return 1

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')

def adcionar_livro():
        novo_id = gerar_novo_id(dados)
        titulo = input("Informe o Título do livro:\n").lower()
        autor = input("Informe o Autor do livro:\n").lower()
        dataNascimento = input("informe a data de nascimento do Autor!\n")
        livros = {
                "id": novo_id,
                "titulo": titulo,
                "autor": autor,
                "data_Cadastro": data,
                "Disponivel": True
            }
        autores = {
             "id": novo_id,
             "autor": autor,
             "data_Nascimento":dataNascimento
        }
        dados["Livros"].append(livros)
        dados["Autores"].append(autores)
        salvar_dados(dados)
        limpar_tela()
        return

def listar_livro():
    dados 
    if dados["Livros"]:
        print("\nLista de Livros")
        for paginas in dados["Livros"]:
            print(f"titulo: {paginas['titulo']}, Autor: {paginas['autor']}, data_Cadastro: {paginas['data_Cadastro']}\n")
    else:
        print("Nenhum livro dentro da lista!")

def listar_Autores():
    dados
    if dados["Autores"]:
        print("\nLista de Autores")
        for paginas in dados["Autores"]:
            print(f"ID: {paginas['id']}, Autor: {paginas['autor']}, Data de Nascimentos: {paginas['data_Nascimento']}\n")
    else:
        print("Nenhum Autor foi adcionado para listar!")

def deletar_livro():
    dados
    if dados["Livros"]:
        print("\nLivros cadastrados:")
        for paginas in dados["Livros"]:
            print(f"ID: {paginas['id']}, titulo: {paginas['titulo']}")

        id_para_deletar = input("Digite o ID do livro que deseja deletar: ")

        livro_encontrado = False
        for livro in dados["Livros"]:
            if str(livro["id"]) == str(id_para_deletar):
                dados["Livros"].remove(livro)
                livro_encontrado = True

                for autor in dados["Autores"]:
                    if str(autor["id"]) == str(id_para_deletar):
                        dados["Autores"].remove(autor)
                        break
                break
        if livro_encontrado:
            salvar_dados(dados)
            print("Livro deletado com sucesso.")
        else:
            print("ID não encontrado. Nenhum livro foi deletado.")
    else:
        print("\nNenhum livro cadastrado.")

def realizar_emprestimo():
    dados
    print("Livros disponíveis para empréstimo:")
    for livro in dados["Livros"]:
        if livro["Disponivel"]:
            print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}")
    id_livro = int(input("Digite o ID do livro que deseja emprestar: "))

    if str(livro["id"]) == str(id_livro):
        if livro["Disponivel"]:
            livro["Disponivel"] = False
            print(f"O livro '{livro['titulo']}' foi emprestado com sucesso!")
            dados['Emprestimos'].append('Livros')
            salvar_dados(dados)
            return
        else:
            print(f"O livro '{livro['titulo']}' já está emprestado e indisponível.")
            return

def listar_livros_disponiveis():
    dados  
    livros_disponiveis = False  

    print("Livros disponíveis para empréstimo:")
    for livro in dados["Livros"]:
        if livro["Disponivel"]:
            print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}")
            livros_disponiveis = True  
    
    if not livros_disponiveis:
        print("Nenhum livro registrado")

def buscar_livro():
    dados
    buscar = input("Digite o Título ou nome do autor:\n").lower()
    limpar_tela()
    encontrou = False
    
    for livro in dados["Livros"]:
        if (buscar in livro["titulo"].lower() or buscar in livro["autor"].lower()):
            if livro["Disponivel"]:
                print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]} - Disponível para empréstimo!')
                encontrou = True
                salvar_dados(dados)

            else:
                print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]} - Já está emprestado.')
                encontrou = True
                
        if not encontrou:
            print("Nenhum livro encontrado com o título ou autor informado.")

def listar_livros_emprestados():
    dados
    livros_emprestados = False  

    print("Livros atualmente emprestados:")
    for livro in dados["Livros"]:
        if not livro["Disponivel"]:
            print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}")
            livros_emprestados = True  

    if not livros_emprestados:
        print("Nenhum livro emprestado no momento.")

def retirar_emprestimo():
    dados
    listar_livros_emprestados() 
    id_para_retirar = input("Digite o ID do livro que deseja retirar do empréstimo: ")

    livro_encontrado = False
    for livro in dados["Livros"]:
        if str(livro["id"]) == str(id_para_retirar) and not livro["Disponivel"]:
            livro["Disponivel"] = True
            livro_encontrado = True
            print(f"O livro '{livro['titulo']}' foi retirado do empréstimo e está disponível novamente.")
            break
    if not livro_encontrado:
        print("ID não encontrado ou o livro já está disponível.")

    salvar_dados(dados)