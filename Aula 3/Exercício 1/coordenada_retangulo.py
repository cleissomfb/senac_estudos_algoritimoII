#Verificar se um ponto colidiu com um retângulo ou não

ponto_cordenadaX = int(input ("Digite a coordenada X do ponto: "))
ponto_cordenadaY = int(input ("Digite a coordenada Y do ponto: "))

retangulo_coordenadaX = int(input ("Digite a coordenada X do retângulo: "))
retangulo_coordenadaY = int(input ("Digite a coordenada Y do retângulo: "))

retangulo_dimencaoX = int(input ("Digite a dimenção X do retângulo: "))
retangulo_dimencaoY = int(input ("Digite a dimenção Y do retângulo: "))

ponto_cordenadaX = ponto_cordenadaX - retangulo_coordenadaX
ponto_cordenadaY = ponto_cordenadaY - retangulo_coordenadaY

if (ponto_cordenadaX * ponto_cordenadaY) + (ponto_cordenadaY * ponto_cordenadaY) <= (retangulo_dimencaoX * retangulo_dimencaoY) :
    print ("O ponto está dentro do retângulo.")
else:
     print ("O ponto está não está dentro do retângulo.")
