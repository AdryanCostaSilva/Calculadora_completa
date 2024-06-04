import numpy as np
import matplotlib.pyplot as plt

def linha():
    print("=" * 60)


def raizes_seggrau(a,b,c):
    d = (b**2)-4*a*c
    if d < 0:
        print("Não possuí raízes reais: ")
    x1 = (-b+d**(1/2))/(2*a)
    x2 = (-b-d**(1/2))/(2*a)
    print(f"X1 = {x1:.2f}")
    print(f"X2 = {x2:.2f}")


def fx_calculado(a,b,c,x):
    y = a*(x**2)+(b*x)+c
    return y


def maxmin_seggrau(a,b,c):
    d = (b**2)-(4*a*c)
    xv = -b/(2*a)
    yv = -d/(4*a)
    print(f"x do vétice tem valor: {xv}\ny do vértice tem o valor: {yv}")
    if a < 0:
        print("A função tem um valor máximo.")
    elif a > 0:
        print("A função tem um valor minimo.")


def menu_segundograu():
    while True:
        print("f(x)= ax² + bx + c")
        a = float(input("Informe o coeficiente (a) da função: "))
        b = float(input("Informe o coeficiente (b) da função: "))
        c = float(input("Informe o coeficiente (c) da função: "))
        while True:
            linha()
            print("ESCOLHA UMA OPERAÇÃO PARA A FUNÇÃO DO 2º GRAU".center(60))
            linha()
            oc = str(input(f" [1] Calcular raízes \n [2] Cálcular função em X pedido\n [3] Calcular Vértice\n [4] Gerar gráfico\n \n [5] Informar outra função de 2º grau\n [6] Sair para menu inicial\n >>> "))
            if oc not in "123456":
                    print("Operação inválida! Tente novamente.")
                    continue
            elif oc == "1":
                raizes_seggrau(a,b,c)
            elif oc == "2":
                x = int(input("Dígite um número (X): "))
                y = fx_calculado(a,b,c,x)
                print(f"O valor de f em função de x é: {y}")
            elif oc == "3":
                maxmin_seggrau(a,b,c)
            elif oc == "4":
                def f(x):
                    y = a*(x**2)+(b*x)+c
                    return y
                      #Criando o nosso domínio (Eixo X)
                eixoX = np.arange(-1200,1500,1)
                print(eixoX)

                eixoY = []
                for x in eixoX:
                    y = f(x)
                    eixoY.append(y)

                print(eixoY)
                plt.plot(eixoX, eixoY, label = "F(x)= ax² + bx + c", color = 'b')
                #Título do gráfico
                plt.title("Função do primeiro grau: F(x)= ax² + bx + c")
                plt.legend()
                #Títulos dos eixos
                plt.xlabel("eixo x")
                plt.ylabel("eixo y")
                #Colocar grade no gráfico
                plt.grid(True)
                #Adicionar linha dos eixos
                plt.axhline(y=0,color='k')
                plt.axvline(x=0,color='k')

                #Mostrar gráfico
                plt.show()
                
            elif oc == "5":
                break
            
            elif oc == "6":
                break  
        if oc == 6:
            break

        
menu_segundograu()

