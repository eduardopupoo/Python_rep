import os

def exibe_nome_aplicacao():
    print("""

SABOR EXPRESS

""")
def exibe_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def escolher_opcao():
    opcao_escolhida = int(input ("Escolha uma opção: \n"))
    print(f"Você escolheu a opção: {opcao_escolhida}.")

    def finalizar_app():
        print('Fechando a aplicação...')
        print()

    if opcao_escolhida == 1:
        print ("Cadastrar um restaurante")
    elif opcao_escolhida == 2:
        print ("Listar restaurantes")
    elif opcao_escolhida == 3:
        print ("Ativar restaurante")

    finalizar_app()

def main():
    exibe_nome_aplicacao()
    exibe_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
