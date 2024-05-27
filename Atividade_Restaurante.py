import os
 
#restaurantes = [ 'BK' , 'KFC', ]
 
restaurantes = [{},
                {},
                {},
                {}]
 
 
def mostrar_nome_do_sistema():
    print("""
           
        ██████╗  █████╗ ███████╗████████╗ █████╗ ██████╗ ██╗████████╗██╗███████╗███████╗
        ██╔══██╗██╔══██╗╚══███╔╝╚══██╔══╝██╔══██╗██╔══██╗██║╚══██╔══╝██║██╔════╝██╔════╝
        ██████╔╝███████║  ███╔╝    ██║   ███████║██████╔╝██║   ██║   ██║█████╗  ███████╗
        ██╔═══╝ ██╔══██║ ███╔╝     ██║   ██╔══██║██╔══██╗██║   ██║   ██║██╔══╝  ╚════██║
        ██║     ██║  ██║███████╗   ██║   ██║  ██║██║  ██║██║   ██║   ██║███████╗███████║
        ╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝
        """)

def mostrar_opcoes():
    print('1. Adicionar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def sair_app():
    os.system('cls')
    print('Finalizando o sistema')

def retornar_menu_principal():
    input('Pressione qualquer tecla para voltar ao menu principal')
    principal()  

def opcao_incorreta():
    print('Opção Inválida!\n')
    retornar_menu_principal()

def mostrar_subtitulo(texto):    
    os.system('cls')
    print(texto)

def adicionar_restaurante():
    mostrar_subtitulo('Adicionar novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja adicionar: ')
    categoria = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    dados_restaurante =  {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi adicionado com sucesso!')
    retornar_menu_principal()

def listar_restaurantes():
    mostrar_subtitulo('Listando os restaurantes\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante.get('nome', 'Desconhecido')
        categoria = restaurante.get('categoria', 'Desconhecida')
        ativo = restaurante.get('ativo', False)
        print(f'| {nome_restaurante} | {categoria} | {"Ativo" if ativo else "Inativo"} |')
    retornar_menu_principal()

def selecionar_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            adicionar_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            alterar_estado_restaurante()
        elif opcao == 4:
            sair_app()
        else:
            opcao_incorreta()
    except ValueError:
        opcao_incorreta()

def alterar_estado_restaurante():
    mostrar_subtitulo('Alterar estado do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante.get('nome'):
            encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            status = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'O restaurante {nome_restaurante} foi {status} com sucesso!')
            break
    if not encontrado:
        print('Restaurante não encontrado!')
    retornar_menu_principal()

def main():
    os.system('cls')
    mostrar_nome_do_sistema()
    mostrar_opcoes()
    selecionar_opcao()

if __name__ == '__main__':
    main()