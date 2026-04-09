# Jogo de adivinhação
# O programa irá gerar um número aleatório de 0 a 10
# E o jogador tenta acertar qual é
# Caso o jogador acerte, o programa irá parar e mostrará as tentativas
# Se o jogador excede o número de tentativas o programa irá relatar e vai parar
# de executar
import random
import os

while True:
    try:
        print("---- Jogo de Adivinhação ----")
        print("Acerte um número aleatório de 0 a 10")
        print("Digite [1] para inicar o programa\nDigite [2] para Sair")
        digito = int(input("Escolha uma opção: "))
        if digito == 2:
            print("Você saiu")
            break

        elif digito == 1:
            os.system("cls")
            print("Programa INICIADO")
            
            numero_aleatorio_gerado = random.randint(0,10)
            tentativas = 5

            while tentativas > 0:
                try:
                    escolha_de_numeros = int(input("Qual o número gerado?: "))
                    if escolha_de_numeros == numero_aleatorio_gerado:
                        print("PARABÉNS!! Você acertou")
                        print(f"O número gerado era {numero_aleatorio_gerado}")
                        break
                    else:
                        tentativas -= 1
                        if tentativas > 0:
                            print("Tente novamente")
                            print(f"Você ainda tem {tentativas} tentativas")
                            continue
                        
                        elif tentativas == 0:
                            print("Você excedeu o número de tentativas")
                            print(f"O número aleatorio gerado era {numero_aleatorio_gerado}")
                            break
                except ValueError:
                    print("Digite apenas um número inteiro")
        else:
            print("Digite apenas a opção [1] ou opção [2]")

    except ValueError:
            print("Digite apenas um número inteiro")
    print()