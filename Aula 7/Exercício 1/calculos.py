
class Calculos:

    def __init__(self):
        self.matrizA = []
        self.matrizB = []
        self.matrizC = []

    def cria_matrizC(self, linhas, colunas, valor):
        M = []
        while linhas > 0:
            M.append([valor] * colunas)
            linhas -= 1
        return M

    def multiplica_matriz(self, matrizA, matrizB):
        self.matrizA = matrizA
        self.matrizB = matrizB

        linhas = len(self.matrizA)
        colunas = len(self.matrizB[0])
        if linhas != colunas:
            print("Não tem solução")
        self.matrizC = self.cria_matrizC(linhas, colunas, 0)
        for x in range(colunas):
            for y in range(linhas):
                for r in range(colunas):
                    self.matrizC[x][y] += self.matrizA[x][r] * self.matrizB[r][y]
        return self.matrizC
