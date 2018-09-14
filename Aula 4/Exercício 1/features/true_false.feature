# language: pt

Funcionalidade: Verificar se os números da lista são par ou impar

    Cenario: verificar numeros pares e impares
    Dado uma lista de números randomicos
    Quando verifico se são pares ou impares
    Então todos os pares são True e todos os impares são False
