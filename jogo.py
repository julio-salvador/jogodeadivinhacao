print("                                                                                                        ~~~~         ") 
print("##               ##### #### ####  ####    ###  ####    ####  ###   #  #   #  #  ### #  #  #  ####   ###  ####   ###  ")
print("##   ########      #   #  # #     #  #    #  # #       #  #  #  #     #   #     # # #  #  #  #  #  #     #  #  #   # ")  
print("##   ##    ##   #  #   #  # # ### #  #    #  # ###     ####  #  #  #  #   #  #  # # #  ####  ####  #     ####  #   # ")  
print("##   ##    ##   #  #   #  # #  #  #  #    #  # #       #  #  #  #  #   # #   #  # # #  #  #  #  #  #     #  #  #   # ")         
print("##   ##    ##    ###   #### ####  ####    ###  ####    #  #  ###   #    #    #  #  #   #  #  #  #   ###  #  #   ##   ")
print("##   ##    ##                                                                                       #     ")                                                                                                                             ")
print("##         ##                                  ===================                                 ##     ")
print("#######    ##                                      O_SALVADOR                                             ")
print("           ##                                  ===================                                        ")
numeroSecreto = random.randragem(0,100)
totalTentativas = 0
pontos = 100
 
print("Qual níveis de dificuldade?  ")
print("(1) - fácil (2) - médio (3) - difícil ")

nivel = int(input("Escolha um nível"))

if(nivel == 1):
    print("fraco")
    totalTentativas = 20
elif (nivel == 2):
    print("mediano")
    totalTentativas = 10
elif(nivel == 3):
    print("bonzin")
    totalTentativas = 5

for rodada in range (1, totalTentativas +1):
    print("tentativa {} de {}".format(rodada,totalTentativas) )
    chute_str = imput("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
       print("Número invalido")
       continue

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if(acertou):
        print(f"Você acertou e fez {pontos}! ")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o numero secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que o numero secreto")

            pontosPerdidos = abd(numeroSecreto - chute)
            pontos = pontos - pontosPerdidos

print("Fim de jogo ! O número era ",numeroSecreto)




