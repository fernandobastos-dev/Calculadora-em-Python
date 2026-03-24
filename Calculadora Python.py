#calculadora

num1 = (int(input("digite o primeiro numero:")))
num2 = (int(input("digite o segundo numero:")))
operação = input("digite a operação:")

match operação:
    case  "+":
        res = num1 + num2
    case  "-":
        res = num1 - num2
    case  "*":
        res = num1 * num2
    case  "/":
        if num2 != 0:
            res = num1 / num2
        else:
            print("Erro: divisão por zero!")
            exit()

    case _:
        print("Operação inválida")
        exit()

print(f"resultado é igual a {res}")
