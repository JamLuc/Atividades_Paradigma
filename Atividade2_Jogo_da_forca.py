import os
import random

class Tentativas:
    quantidade_vezes = 5

Lista_palavras_Comidas = ['bisteca', 'arroz', 'pizza', 'pastel', 'macarrão']
Lista_palavras_Cores = ['vermelho', 'azul', 'verde', 'amarelo', 'preto']
Lista_palavras_Frutas = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']
Temas = ['Comida', 'Cor', 'Fruta']

def inicio_jogo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bem-vindo ao jogo da Forca!")
    lista_palavras, tema = escolhendo_tema()
    palavra_secreta = escolher_palavra(lista_palavras)
    print(f"O tema da vez é: {tema}. Boa sorte!")
    jogo(palavra_secreta)

def escolhendo_tema():
    tema = random.choice(Temas)
    if tema == 'Comida':
        return Lista_palavras_Comidas, tema
    elif tema == 'Cor':
        return Lista_palavras_Cores, tema
    elif tema == 'Fruta':
        return Lista_palavras_Frutas, tema

def escolher_palavra(lista_palavras):
    return random.choice(lista_palavras)

def desenhar_forca(tentativas_restantes):
    estagios = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
              |
        -----------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
              |
        -----------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
              |
        -----------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
              |
        -----------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
              |
        -----------
        """,
        """
           -----
           |   |
           O   |
               |
               |
              |
        -----------
        """
    ]
    print(estagios[tentativas_restantes])

def exibir_forca(tentativas_restantes, palavra_oculta):
    desenhar_forca(tentativas_restantes)
    print(f"\nPalavra: {palavra_oculta}")
    print(f"Tentativas restantes: {tentativas_restantes}")

def jogo(palavra_secreta):
    tentativas_restantes = Tentativas.quantidade_vezes
    palavra_oculta = "_" * len(palavra_secreta)
    letras_adivinhadas = []

    while tentativas_restantes > 0 and "_" in palavra_oculta:
        exibir_forca(tentativas_restantes, palavra_oculta)
        letra = input("Digite uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra.")
        elif letra in palavra_secreta:
            letras_adivinhadas.append(letra)
            palavra_oculta = "".join([letra if letra in letras_adivinhadas else "_" for letra in palavra_secreta])
        else:
            letras_adivinhadas.append(letra)
            tentativas_restantes -= 1

    if "_" not in palavra_oculta:
        print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
    else:
        exibir_forca(tentativas_restantes, palavra_oculta)
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

def main():
    inicio_jogo()

if __name__ == '__main__':
    main()
