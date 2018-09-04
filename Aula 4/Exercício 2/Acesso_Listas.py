
num_array = []

def menu_principal():
    print ("\n1 - Digitar uma lista de números")
    print ("2 - Visualizar a lista de números")
    print ("3 - Vizualizar maior número e seu indice da lista")
    print ("4 - Vizualizar menor número e seu indice da lista")
    print ("5 - Vizualizar a soma dos números pares")
    print ("6 - Vizualizar a soma dos números impares")
    print ("7 - Vizualizar a soma da divisão dos números de indice par pelos de indice impar")
    print ("8 - Vizualizar a lista na ordem inversa")
    print ("0 - Sair do programa")
    item_menu = (int(input("\nDigite uma opção do menu: ")))

    if (item_menu == 0):
        sys.exit()
    elif (item_menu == 1):
        digitacao_array_num()
        menu_principal()
    elif (item_menu == 2):
        print ("\nA lista original é: ", str(num_array).strip("[]"))
        menu_principal()
    elif (item_menu == 3):
        print ("\nO número maior é ", valor_maior() , "e o seu indice é: ", indice_maior())
        menu_principal()
    elif (item_menu == 4):
        print ("\nO número menor é ", valor_menor() , "e o seu indice é: ", indice_menor())
        menu_principal()
    elif (item_menu == 5):
        print ("\nA soma dos números pares é:", soma_pares())
        menu_principal()
    elif (item_menu == 6):
        print ("\nA soma dos números impares é: ", soma_impares())
    elif (item_menu == 7):
        #print ("A divisão dos indices impares pelos indices pares é: ", divisao_indice_par_impar())
        menu_principal()
    elif (item_menu == 8):
        print ("\nA impressão inversa do array é: ", str(impressao_inversa_array()).strip("[]"))
    else:
        print("\nMenu inválido, tente novamente!")
        menu_principal()

def digitacao_array_num():
    indice = 0
    for i in range(5):
        print ("\nLista de números do array:", indice+1,":10")
        num_array.append(int(input("Digite um número: ")))
        indice += 1
    else:
        print("\nLista cheia\n")

    #while indice < 10:
    #num = int(input("Digite um número: "))
    #indice += 1
    #num_array.append(num)

def valor_maior():
    #iMaior = max(num_array)
    iMaior = num_array[0]
    for valor_maior in num_array:
        if valor_maior > iMaior:
            iMaior = valor_maior
    return iMaior

def valor_menor():
    #iMenor = min(num_array)
    iMenor = num_array[0]
    for valor_menor in num_array:
        if valor_menor < iMenor:
            iMenor = valor_menor
    return iMenor

def indice_maior():
    indice_Maior = 0
    for indice_maior in range(len(num_array)):
        if valor_maior() == num_array[indice_maior]:
            indice_Maior = indice_maior
    return indice_Maior

def indice_menor():
    indice_Menor = 0
    for indice_menor in range(len(num_array)):
        if valor_menor() == num_array[indice_menor]:
            indice_Menor = indice_menor
    return indice_Menor

def soma_pares():
    soma_num_pares = 0
    for indice_soma_pares in num_array:
        if indice_soma_pares % 2 == 0:
            soma_num_pares += indice_soma_pares
    return soma_num_pares

def soma_impares():
    soma_num_impares = 0
    for indice_soma_impares in num_array:
        if indice_soma_impares % 2 == 1:
            soma_num_impares += indice_soma_impares
    return soma_num_impares

#def divisao_indice_par_impar():

def impressao_inversa_array():

    #array_aux = [num_array[-i] for i in range(1, len(num_array) + 1)]

    #inicio = 0
    #fim = len(num_array) - 1
    #while inicio < fim:
    #num_array[inicio], num_array[fim] = num_array[fim], num_array[inicio]
    #inicio += 1
    #fim -= 1

    array_aux = num_array[::-1]
    return array_aux

print ("\nLista de Arrays\n")

menu_principal()
