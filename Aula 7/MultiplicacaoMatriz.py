

matrizA = []
matrizB = []
matrizC = []


def cria_matriz(linhas, colunas, valor):
    M = []
    while linhas > 0:
        M.append([valor] * colunas)
#        m = [([0] * j) * i]
        linhas -= 1
    return M


def multiplica_matriz(matrizA, matrizB):

    linhas = len(matrizA)
    colunas = len(matrizB[0])
    if linhas != colunas:
        print("Não tem solução")
    matrizC = cria_matriz(linhas, colunas, 0)
    for x in range(colunas):
        for y in range(linhas):
            for r in range(colunas):
                matrizC[x][y] += matrizA[x][r] * matrizB[r][y]
    return matrizC


def main():

    matrizA = cria_matriz(5, 4, 2)
    matrizB = cria_matriz(4, 5, 2)
    matrizC = multiplica_matriz(matrizA, matrizB)


#main()

matrizA = cria_matriz(5, 4, 2)
matrizB = cria_matriz(4, 5, 2)
matrizC = multiplica_matriz(matrizA, matrizB)

print("\nMatriz A: ", matrizA)
print("Matriz B: ", matrizB)
print("Matriz C = Matriz A * Matriz B: ", matrizC)
