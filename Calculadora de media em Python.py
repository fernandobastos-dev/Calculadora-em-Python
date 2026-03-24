


# Função que calcula a média de quatro notas
def calcularMedia(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

# Programa principal
print("Bem-vindo à Calculadora de Média!")

# Pedir as quatro notas ao usuario
nota1 = float(input("Introduza a primeira nota: "))
nota2 = float(input("Introduza a segunda nota: "))
nota3 = float(input("Introduza a terceira nota: "))
nota4 = float(input("Introduza a quarta nota:. "))

# Calcular a média usando a função
media_final = calcularMedia(nota1, nota2, nota3, nota4)

# Exibir o resultado
print(f"A média das quatro notas é: {media_final:.3f}")


### Explicação:
# Usei uma **função** chamada `calcularMedia` que recebe quatro notas e devolve a média.
# O utilizador insere as três notas, que são guardadas em variáveis.
# Chamamos a função passando as notas, e mostramos a média com duas casas decimais (`:.3f`).
