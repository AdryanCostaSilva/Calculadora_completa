import numpy as np
import matplotlib.pyplot as plt
def linha():
    print("=" * 60)
def funcao_exponencial ():
    while True:
        ae = float(input("Informe o coeficiente (a) da função: "))
        while True:
            linha()
            print("ESCOLHA UMA OPERAÇÃO PARA A FUNÇÃO EXPONENCIAL".center(60))
            linha()
            oc = str(input(f" [1] Verificar se é crescente ou decrescente \n [2] Cálcular função em X pedido\n [3] Gerar gráfico\n \n [4] Informar outra função exponencial\n [5] Sair para menu inicial\n >>> "))
            if oc not in "123456":
                print("Operação inválida! Tente novamente.")
                continue
            elif oc == "1":
                if ae > 1:
                    print("A função é Crescente!")
                elif ae > 0 and ae < 1:
                    print("A função é Decrescente!")
            elif oc == "2":
                x = float(input("Informe o (x) da função: "))
                y = ae**x
                print(y)
            elif oc == "3":
                def f(x):
                    x = float(input("Informe o (x) da função:  "))
                    y = ae**x
                    return y
                #Criando o nosso domínio (Eixo X)
                eixoX = np.arange(-10,11,1)
                print(eixoX)

                eixoY = []
                y = f(x)
                eixoY.append(y)

                print(eixoY)
                plt.plot(eixoX, eixoY, label = "f(x) = 2x+1", color = 'b')
                #Título do gráfico
                plt.title("Função do primeiro grau: 2x+1")
                plt.legend()
                #Títulos dos eixos
                plt.xlabel("eixo x")
                plt.ylabel("eixo y")
                #Colocar grade no gráfico
                plt.grid(True)
                #Adicionar linha dos eixosaw
                plt.axhline(y=0,color='k')
                plt.axvline(x=0,color='k')

                #Mostrar gráfico
                plt.show()
            elif oc == "4":
                break
            elif oc == "5":
                break    
        if oc == "5":
            break                    
                            
funcao_exponencial()