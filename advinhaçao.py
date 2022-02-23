import random

def mensagem_abertura():
    print("**********************************")
    print("Bem-vindo ao jogo da advinhação!!!")
    print("**********************************")

def gerador_numero_secreto():
    numero_secreto = random.randrange(1, 101)
    return numero_secreto

def seleção_dificuldade():
    total_de_tentativas = 0
    seleçaõ_dificuldade = int(input("Escolha sua dificuldade!!! Facil (1), Medio (2), Dificil (3) "))
    
    if(seleçaõ_dificuldade == 1):
        total_de_tentativas = 15
    elif(seleçaõ_dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    return total_de_tentativas

########################

def chute_jogador():
    chute = int(input("Digite o seu numero: "))
    print(chute)
    return chute   

#########################

def jogar_advinhaçao():


    pontos = 500
    mensagem_abertura()
    numero_secreto = gerador_numero_secreto()
    total_de_tentativas = seleção_dificuldade()
   
    for rodada in range (1, total_de_tentativas + 1):
        chute = chute_jogador()
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        if(chute > 100 or chute < 1):
            print("Voce deve digitar um numero de 1 a 100")
            continue

        if(chute == numero_secreto):
            print("Parabens, voce conseguiu o minimo e fez {} pontos".format(pontos))
            break
        else:
            pontos_perdidos = abs(chute - numero_secreto)
            pontos = pontos - pontos_perdidos
            if(chute > numero_secreto):
                print("O seu chute foi maior do que o numero secreto")
                if(total_de_tentativas == rodada):
                    print("voce é podre e so conseguiu {} pontos".format(pontos))
            elif(chute < numero_secreto):
                print("O seu chute foi menor do que o numero secreto")
                if(total_de_tentativas == rodada):
                    print("Voce é podre e so conseguiu {} pontos".format(pontos))

#######################

if(__name__ == "__main__"):
    jogar_advinhaçao()