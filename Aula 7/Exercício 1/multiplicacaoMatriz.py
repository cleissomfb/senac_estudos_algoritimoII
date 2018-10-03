
from calculos import Calculos

matrizA = []
matrizB = []
matrizC = []


def cria_matrizes(linhas, colunas, valor):
    M = []
    while linhas > 0:
        M.append([valor] * colunas)
        linhas -= 1
    return M


def main():
    calcula = Calculos()
    matrizA = cria_matrizes(5, 4, 2)
    matrizB = cria_matrizes(4, 5, 2)
    matrizC = calcula.multiplica_matriz(matrizA, matrizB)
    print(matrizC)


main()
