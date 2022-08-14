def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças jogadas? "))
    cond = True
    
    if (n % (m + 1) == 0):
        print("Você começa!!!")
        cond_player = True
        tirar = usuario_escolhe_jogada(n, m)
        print("Você tirou", tirar)
        n = n - tirar
        if n <= 0:
            print("Você ganhou!")
            point_player = "jogador"
            return(point_player)
    else:
        cond_player = False
        print("Computador começa!!!")
        tirar = computador_escolhe_jogada(n, m)
        print("Computador tirou", tirar)
        n = n - tirar
        if n <= 0:
            print("computador ganhou!")
            point_computer = "computador"
            return(point_computer)
        else:
            print("Sobrou", n)
            
    if not cond_player:
        while cond:
                tirar = usuario_escolhe_jogada(n, m)
                print("Você tirou", tirar)
                n = n - tirar
                if n <= 0:
                    print("Você ganhou!")
                    point_player = "jogador"
                    return(point_player)
                    cond = False
                else:
                    print("Sobrou", n)
                    tirar = computador_escolhe_jogada(n, m)
                    print("Computador tirou", tirar)
                    n = n - tirar
                    if n <= 0:
                        print("computador ganhou!")
                        point_compuint = "computador"
                        return(point_compuint)
                        cond = False
                    else:
                        print("Sobrou", n,"peças.")
    else:
        while cond:
            tirar = computador_escolhe_jogada(n, m)
            print("Computador tirou", tirar)
            n = n - tirar
            if n <= 0:
                print("computador ganhou!")
                point_compuint = "computador"
                return(point_compuint)
                cond = False
            else:
                print("Sobrou", n,"peças.")
                tirar = usuario_escolhe_jogada(n, m)
                print("Você tirou", tirar)
                n = n - tirar
                if n <= 0:
                    print("Você ganhou!")
                    point_player = "jogador"
                    return(point_player)
                    cond = False
                else:
                    print("Sobrou", n)

def usuario_escolhe_jogada(n, m):
    while n != 0:
        tirar = int(input("Quantas peças você vai tirar? "))
        if tirar > n or tirar > m or tirar <= 0:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            return(tirar)

def computador_escolhe_jogada(n, m):
    jogada = m
    cond = True
    
    while jogada != 0 and cond:
        if ((n - jogada) % (m + 1) == 0):
            cond = False
            return(jogada)
        else:
            jogada = jogada - 1
    if jogada == 0:
        return(m)
    
def inicio():
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    print("")
    cond = True
    placar_computer = 0
    placar_player = 0
    
    while cond:
        print("1- para jogar uma partida isolada")
        print("2- para jogar um campeonato")
        mode = input("")
        print("")
        
        if mode == "1":
            print("Voce escolheu uma partida isolada! ")
            partida()
            cond = False
        else:
            if mode == "2":
                print("Voce escolheu um campeonato!")
                
                print("**** Rodada 1 ****")
                if partida() == "computador":
                    placar_computer = placar_computer + 1
                else:
                    placar_player = placar_player + 1
                
                print("**** Rodada 2 ****")
                if partida() == "computador":
                    placar_computer = placar_computer + 1
                else:
                    placar_player = placar_player + 1
                    
                print("**** Rodada 3 ****")
                if partida() == "computador":
                    placar_computer = placar_computer + 1
                else:
                    placar_player = placar_player + 1
                    
                print("****Final do campeonato! ****")
                print("Placar: Você", placar_player,"X", placar_computer, "Computador")
                cond = False
            else:
                print("Oops! Escolha inválida! Tente de novo.")
inicio()
