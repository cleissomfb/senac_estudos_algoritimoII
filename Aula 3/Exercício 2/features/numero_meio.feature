# language: pt

Funcionalidade: Retornar o numero do meio de uma lista de 3 numeros diferentes.
  Cenario: O numero do meio esta em primeiro lugar.
    Dada uma lista com os numeros (3,1,2)
    Quando queremos saber o numero da esquerda
    Então o resultado e 3

    Cenario: O numero do meio esta em terceiro lugar
      Dada uma lista com os numeros (9,8,7)
      Quando queremos saber o numero da direita
      Então o resultado e 7

    Cenario: O numero do meio esta no meio
      Dada uma lista com os numeros (6,5,4)
      Quando queremos saber o numero que esta no meio
      Então o resultado e 5
