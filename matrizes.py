def linha():
    print("=" * 60)

#Imprimindo a matriz
def imprir_matriz(matriz):
    for linha in matriz:
        print(linha)


#Gerando a matriz
def gerarMatriz(quantlinhas,quantcolunas):
    matriz = []
    for i in range(quantlinhas):
        linha = []
        for j in range(quantcolunas):
            numero = int(input(f"Informe uma valor para linha {i} e coluna {j}\n"))
            linha.append(numero)
        matriz.append(linha)
    return matriz


#Verificando se a matriz é quadrada
def verificar_matriz_quadrada(matriz):
    linha = 0
    coluna = 0
    for i in matriz:
        linha += 1
    for j in matriz[0]:
        coluna += 1
    if linha == coluna:
        return True
    else:
        return False


#Calculando a determinante da matriz
def determinantecalc(matriz, linhas, colunas):
    if linhas == 3 and colunas == 3:
        determinante = (matriz[0][0] * matriz[1][1] * matriz[2][2] +\
                        matriz[0][1] * matriz[1][2] * matriz[2][0] +\
                        matriz[0][2] * matriz[1][0] * matriz[2][1]) -\
                        (matriz[0][2] * matriz[1][1] * matriz[2][0] +\
                        matriz[0][0] * matriz[1][2] * matriz[2][1] +\
                        matriz[0][1] * matriz[1][0] * matriz[2][2])
        return determinante
    elif linhas == 2 and colunas == 2:
        determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        return determinante
    else:
        if linhas != colunas:
            return False


#Multiplicando as matrizes
def multiplicação_matriz(matriz1, matriz2):
    matriz_multiplicada = []
    for i in range(0, len(matriz1)):
        matriz_multiplicada.append([])
        for j in range(len(matriz2[0])):
            matriz_multiplicada[i].append(0)
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                matriz_multiplicada[i][j] += matriz1[i][k] * matriz2[k][j]
    return matriz_multiplicada


#Transposta da matriz
def tranposta_matriz(matriz):
    transposta = []
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    for j in range(ncolunas):
        transposta.append([])
        for i in range(nlinhas):
            transposta[j].append(0)
    for i in range(0, nlinhas):
        for j in range(0, ncolunas):
            transposta[j][i] = (matriz[i][j])
    return transposta  
    

#Menu da matriz
def menu_matriz():
    while True:
        linhas = int(input("Informe o número de linhas da matriz: \n"))
        colunas = int(input("Informe o número de colunas da matriz: \n"))
        matriz = gerarMatriz(linhas, colunas)
        imprir_matriz(matriz)
        while True:
            linha()
            print("ESCOLHA UMA OPERAÇÃO PARA A MATRIZ".center(60))
            linha()
            oc = str(input(f" [1] Determinante (2x2 ou 3x3): Verificar se é matriz quadrada \n [2] Multiplicação\n [3] Matriz transposta\n \n [4] Informar outra matriz\n [5] Sair para menu inicial\n >>>"))
            linha()
            if oc not in '12345':
                print("Operação inválida! Tente novamente.")
                continue
            if oc == '1':
                determinante = determinantecalc(matriz, linhas, colunas)
                if verificar_matriz_quadrada(matriz) == True:
                    print("Esta matriz é quadrada!")
                elif verificar_matriz_quadrada(matriz) == False:
                    print("Não é possível realizar encontrar o determinante! Informe uma matriz quadrada.")
                    continue
                if determinantecalc == False:
                    print("Matriz inválida! Tente novamente")
                    continue
                else:
                    print(f"A determinante da matriz informada é {determinante}")
            elif oc == "2":
                linhas_seg = int(input("Informe a quantidade de linhas da segunda matriz: "))
                colunas_seg = int(input("Informe a quantidade de colunas da segunda matriz: "))
                if linhas_seg != colunas:
                    print("Não é possível realizar a multiplicação! Tente novamente.")
                else:
                    matriz_seg = gerarMatriz(linhas_seg, colunas_seg)
                    multiplicação = multiplicação_matriz(matriz, matriz_seg)
                    print(f"{matriz} x ", end="")
                    print(f"{matriz_seg} = ", end="")
                    print(f"{multiplicação}")
            elif oc == "3":
                transposta = tranposta_matriz(matriz)
                print("A matriz transposta é:")
                for i in transposta:
                    print(i)
            elif oc == "4":
                break
            elif oc == "5":
                break
            linha()
        if oc == "5":
            break
menu_matriz()