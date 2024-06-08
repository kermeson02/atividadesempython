import random

def escolher_palavra():
    palavras = [
        'desenvolvimento', 'tecnologia', 'logica', 'programacao',
        'tendencias', 'computacao', 'algoritmo', 'dados', 'software', 'hardware', 'computador', 'notebook'
    ]
    return random.choice(palavras)

def exibir_forca(tentativas):
    estagios = [
        '''
          -----
          |   |
          |
          |
          |
          |
        ''',
        '''
          -----
          |   |
          |   O
          |
          |
          |
        ''',
        '''
          -----
          |   |
          |   O
          |   |
          |
          |
        ''',
        '''
          -----
          |   |
          |   O
          |  /|
          |
          |
        ''',
        '''
          -----
          |   |
          |   O
          |  /|\\
          |
          |
        ''',
        '''
          -----
          |   |
          |   O
          |  /|\\
          |  /
          |
        ''',
        '''
          -----
          |   |
          |   O
          |  /|\\
          |  / \\
          |
        '''
    ]
    print(estagios[tentativas])

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    tentativas = 0
    letras_tentadas = []

    print("Bem-vindo ao Jogo da Forca!")
    exibir_forca(tentativas)
    print("Palavra: " + ' '.join(palavra_oculta))

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1

        exibir_forca(tentativas)
        print("Palavra: " + ' '.join(palavra_oculta))
        print("Letras tentadas: " + ', '.join(letras_tentadas))

        if '_' not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra:", palavra)
            break
        if tentativas >= 6:
            print("Você perdeu! A palavra era:", palavra)
            break

    print("Obrigado por jogar!")

jogar()