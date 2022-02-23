import advinhaçao
import forca



print("**********************************")
print("Bem-vindo a biblioteca de jogos!!!")
print("**********************************")

print("(1) Jogo da advinhaçao  (2) Jogo da forca")

jogo = int(input("Selecione o seu jogo: "))

if(jogo == 1):
    print("Voce escolheu o jogo da advinhaçao!!!")   
    advinhaçao.jogar_advinhaçao()
elif(jogo == 2):
    print("Voce escolheu o jogo da forca!!!")
    forca.jogar_forca()

    
