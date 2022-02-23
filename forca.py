import random
def jogar_forca():
    
    mensagem_de_abetura()
    palavra_secreta = sorteio_da_palavra()
    
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
        
    enforcou = False
    acertou = False
    erros = 0
   
    while(not acertou and not enforcou):
        
        chute = chute_jogador()
       
        if(chute in palavra_secreta):
            chute_correto_jogador(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if(acertou):
        mensagem_da_vitoria()
    else:
        mensagem_da_derrota(palavra_secreta)
                        

def mensagem_de_abetura():    
    print("**********************************")
    print("***Bem-vindo ao jogo da forca!!***")
    print("**********************************")

def sorteio_da_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
   
    with open("palavras.txt", "r") as arquivo:    
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

       
    numero = random.randrange(0, len(palavras)) 
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializar_letras_acertadas(palavras):
    return ["_" for letra in palavras]

def chute_jogador():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def chute_correto_jogador(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def mensagem_da_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def mensagem_da_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar_forca()


