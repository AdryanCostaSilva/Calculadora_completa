def linha():
    print("=" * 60)
def trans_float(conjunto):
    lista = conjunto.replace(" ", "")
    lista = lista.split(",")
    floats = []
    cont = -1
    for itens in lista:
        for itens_de_itens in itens:
            if itens_de_itens in "aAbBcCdDeEfFgGhHiIjJkKlLMmNnOopPqQrRsStTuUvVWwxXyYZz ":
                return False
        cont += 1
        floats.append(float(itens))
    return floats


def sub_conj_proprio(list_A, list_B):
    sim_nao = ['sim']
    for itens in list_B:
        if itens in list_A:
            sim_nao[0] = "sim"
        else:
            sim_nao[0] = "não"
            break
    if sim_nao[0] == "sim":
        return True
    elif sim_nao[0] == "não":
        return False
        

def uniao_conjunto(list_A, list_B):
    uniao = []
    for itens in list_A:
        if itens not in uniao:
            uniao.append(itens)
    for itens in list_B:
        if itens not in uniao:
            uniao.append(itens)
    return uniao


def interseccao_conjunto(list_A, list_B):
    interseccao = []
    for itens in list_A:
        if itens in list_B:
            if itens not in interseccao:
                interseccao.append(itens)
    if len(interseccao) > 0:
        return interseccao
    else:
        return "Não há intersecção entre os conjuntos."


def diferenca_conjunto(list_A, list_B):
    diferenca = []
    for itens in list_A:
        if itens in list_A and itens not in list_B:
            diferenca.append(itens)
    return diferenca
        
def menu_conjuntos():
    while True:
        linha()
        a = (input("Informe o conjunto A (separando os números com vígula): "))
        b = (input("Informe o conjunto B (separando os números com vígula): "))
        A = trans_float(a)
        B = trans_float(b)
        if trans_float(a) == False:
            print("Conjunto inválido! Tente novamente.")
            linha()
            continue
        elif trans_float(b) == False:
            print("Conjunto inválido! Tente novamente.")
            linha()
            continue
        while True:
            linha()
            print("ESCOLHA UMA OPERAÇÃO PARA OS CONJUNTOS".center(60))
            linha()
            print("Opções:")
            oc = str(input(f" [1] Verificar se A é subconjunto próprio de B \n [2] Realizar operação de União\n [3] Calcular intersecção\n [4] Calcular diferença\n \n [5] Informar outros conjuntos\n [6] Sair para menu inicial\n >>>"))
            linha()
            if oc == "1":
                if sub_conj_proprio(A, B) == True:
                    print("Sim, o conjunto B é subconjunto de A.")
                else:
                    print("Não, o conjunto B não é subconjunto de A.")
            elif oc == "2":
                uniao = uniao_conjunto(A, B)
                print(uniao)
            elif oc == "3":
                interseccao = interseccao_conjunto(A, B)
                print(interseccao)
            elif oc == "4":
                diferenca_a = diferenca_conjunto(A, B)
                diferenca_b = diferenca_conjunto(B, A)
                print(" As diferenças são: ")
                print(f"  A-B: {diferenca_a}")
                print(f"  B-A: {diferenca_b}")
            elif oc == "5":
                A.clear()
                B.clear()
                break
            elif oc == "6":
                break
            elif oc not in "123456":
                print("Operação inválida! Tente novamente.")
                continue
        if oc =="6":
            break
menu_conjuntos()
