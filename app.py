def grade_igual(grade):

    for linha in grade:
        if len(set(linha)) != 1:
            return False

    for coluna in zip(*grade):
        if len(set(coluna)) != 1:
            return False

    diagonal_principal = [grade[i][i] for i in range(len(grade))]
    if len(set(diagonal_principal)) != 1:
        return False

    diagonal_secundaria = [grade[i][len(grade)-i-1] for i in range(len(grade))]
    if len(set(diagonal_secundaria)) != 1:
        return False

def matriz():
    linha1 = [None, None, None]
    linha2 = [None, None, None]
    linha3 = [None, None, None]

    grade = [linha1, linha2, linha3]

    if grade_igual(grade) == grade:
        print("Parabéns você ganhou!!!")

    return grade


def imprimir_grade(grade):
    for elemento in grade:
        print(elemento)


grade = matriz()
imprimir_grade(grade)
grade_igual(grade)

while True:
    while True:
        while True:
            linha = int(input("Digite o número da linha que deseja? "))
            if linha > 2:
                print("Valor %d inválido, digite o número de 0 até 2" % linha)
                continue
            break

        while True:
            coluna = int(input("Digite o número da coluna que deseja? "))
            if coluna > 2:
                print("Valor %d inválido, digite o número de 0 até 2" % coluna)
                continue
            break

        if grade[linha][coluna] is not None:
            print("Posicao ja tem valor. Informe outro valor")
            continue
        break

        while True:
            valor = input("X ou O? ")
        if valor != "x" and valor != "o":
            print("Valor %s inválido, digite X ou O" % valor)
            continue
        break



    grade[linha][coluna] = valor
    imprimir_grade(grade)
    grade_igual(grade)
