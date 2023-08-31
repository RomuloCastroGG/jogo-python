import random       



print('*******************')
print(' BEM VINDO AO JOGO ')
print('*******************')

numero_secreto = random.randrange(1,100)
tentativas = 3
rodada = 1
pontos = 100

print('Qual Nivel de Dificuldade?')
print('(1) Fácil (2) Médio (3) Difícil')

nivel = int(input('Define o nivel: '))

if(nivel == 1):
    tentativas = 10
elif(nivel == 2):
    tentativas = 15
else:
    tentativas = 20

#while (rodada <= tentativas):
for rodada in range(1, tentativas +1):
    print('tentativa {} de {}'. format(rodada, tentativas))
    chute_str = input('Digite um numero de 1 a 100: ')
    print('Você Digitou:', chute_str )
    chute = int(chute_str)

    if chute < 1 or chute >100:
        print('Você deve digitar um numero entre 1 e 100!')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('Você Acertou e fez {} Pontos!'.format(pontos))
        break
    else:
        if (maior):
            print('Você errou! o seu chute foi maior que o numero secreto.')
        elif (menor):
            print('Você errou! o seu chute foi menor que o numero secreto.')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


print('FIM DE JOGO!')
print('O Numero secreto é: {}'.format(numero_secreto))