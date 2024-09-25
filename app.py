# importações
import os
from pessoa import *
from manipulador import *

if __name__ == '__main__':
    # instancia os objetos
    p = Pessoa(0, '', '', '', '')
    m = Manipulador()
    
    usuarios = []  # Variável para armazenar os usuários
    abrir_arquivo = ""  # Variável para armazenar o nome do arquivo aberto

    while True:
        print("1 - Criar um novo arquivo JSON.")
        print("2 - Abrir e ler arquivo JSON.")
        print("3 - Salvar novo usuário.")
        print("4 - Alterar dados do usuário")
        print("5 - Deletar Usuário")
        print("0 - Sair do programa.")

        opcao = input('Informe a opção: ')
        
        os.system('cls')

        match opcao:
            case '0':
                print('Programa encerrado.')
                break
            case '1':
                novo_arquivo = input('Informe o nome do arquivo que deseja criar: ')
                print(m.criar_arquivo(novo_arquivo))
                continuar = input("Deseja abrir este arquivo? (S/N): ").upper()
                if continuar == 'S':
                    abrir_arquivo = novo_arquivo
                    usuarios = m.abrir_arquivo(abrir_arquivo)
                continue
            case '2':
                abrir_arquivo = input('Informe o nome do arquivo que deseja abrir: ')
                try:
                    os.system('cls')
                    usuarios = m.abrir_arquivo(abrir_arquivo)
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    for usuario in usuarios:
                        for campo in usuario:
                            print(f'{campo.capitalize()}: {usuario[campo]}.')
                        print(f'\n{"-"*30}\n')
                except Exception as e:
                    print(f'Não foi possível abrir o arquivo. {e}')
                continue
            case '3':
                if not usuarios:
                    print("Nenhum arquivo aberto. Por favor, abra um arquivo primeiro.")
                    continue
                try:
                    usuario = {}
                    campos = ("nome", "cpf", "email", "profissao")
                    print(f"Arquivo aberto: {abrir_arquivo}.json\n")
                    for campo in campos:
                        usuario[campo] = input(f"Informe o campo {campo.capitalize()}: ")
                    usuario["codigo"] = len(usuarios)
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, abrir_arquivo)) 
                except Exception as e:
                    print(f"Não foi possível realizar a operação. {e}.")
                continue
            case "5":
                if not usuarios:
                    print("Nenhum arquivo aberto. Por favor, abra um arquivo primeiro.")
                    continue
                try:
                    print(f"Arquivo aberto {abrir_arquivo}.json\n")
                    codigo = int(input("Informe o código do usuário que deseja deletar: "))
                    if 0 <= codigo < len(usuarios):
                        nome_deletado = usuarios[codigo]['nome']
                        confirmacao = input(f"Deseja deletar o usuário {nome_deletado}? Digite 'S' para confirmar: ").upper()
                        if confirmacao == 'S':
                            del(usuarios[codigo])
                            print(m.salvar_dados(usuarios, abrir_arquivo))
                            print(f"Usuário {nome_deletado} deletado com sucesso.")
                        else:
                            print(f"Usuário {nome_deletado} não foi excluído.")
                    else:
                        print("Código inválido.")
                except Exception as e:
                    print(f"Não foi possível deletar o usuário. {e}.")
                continue
            case _:
                print('Opção inválida.')
                continue
                