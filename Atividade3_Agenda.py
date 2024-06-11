# Jam Lucas Neves Oliveira
# Arthur Do Santos Sobreira
## Paradigmas de Linguagem de Programção em Python



class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

class AgendaTelefonica:
    def __init__(self):
        self.contatos = []
    
    def apresentacao(self):
        while True:
            print('\n🅐🅖🅔🅝🅓🅐 🅣🅔🅛🅔🅕🅞🅝🅘🅒🅐')
            print('1. Adicionar Contato')
            print('2. Listar Contatos')
            print('3. Sair')
            opcao_escolhida = input('Escolha uma opção: ')
            
            if opcao_escolhida == '1':
                self.adicionar_contato()
            elif opcao_escolhida == '2':
                self.listar_contatos()
            elif opcao_escolhida == '3':
                print('Saindo...')
                break
            else:
                print('Opção inválida. Tente novamente.')

    def adicionar_contato(self):
        nome = input('Digite o nome: ')
        numero = input('Digite o número: ')
        novo_contato = Contato(nome, numero)
        self.contatos.append(novo_contato)
        print(f'Contato adicionado: Nome: {novo_contato.nome}, Telefone: {novo_contato.numero}')

    def listar_contatos(self):
        if not self.contatos:
            print('Nenhum contato na agenda.')
        else:
            print('\nLista de Contatos:')
            for i, contato in enumerate(self.contatos, start=1):
                print(f'{i}. Nome: {contato.nome} | Telefone: {contato.numero}')

if __name__ == "__main__":
    agenda = AgendaTelefonica()
    agenda.apresentacao()

