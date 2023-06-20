def matriz():
    linha1 = [None, None, None]
    linha2 = [None, None, None]
    linha3 = [None, None, None]

    grade = [linha1, linha2, linha3]

    return grade

def imprimir_grade(grade):
    for elemento in grade:
        print(elemento)


def verificar_vitoria():
    ganha_linha = None

    for linha in grade:
        if all(elemento == linha[0] for elemento in linha) and linha[0] is not None:
            ganha_linha = linha[0]
            break

    for coluna in range(3):
        if all(grade[linha][coluna] == grade[0][coluna] for linha in range(3)) and grade[0][coluna] is not None:
            ganha_linha = grade[0][coluna]
            break

    if grade[0][0] == grade[1][1] == grade[2][2] and grade[0][0] is not None:
        ganha_linha = grade[0][0]
    elif grade[0][2] == grade[1][1] == grade[2][0] and grade[0][2] is not None:
        ganha_linha = grade[0][2]
    elif grade[0][0] == grade[1][0] == grade[2][0] and grade[0][0] is not None:
        ganha_linha = grade[0][0]
    elif grade[0][1] == grade[1][1] == grade[2][1] and grade[0][1] is not None:
        ganha_linha = grade[0][1]
    elif grade[0][2] == grade[1][2] == grade[2][2] and grade[0][2] is not None:
        ganha_linha = grade[0][2]
    return ganha_linha

grade = matriz()
imprimir_grade(grade)

while True:
    while True:
        while True:
            linha = int(input("Digite o número da linha que deseja: "))
            if linha > 2:
                print("Valor %d inválido. Digite um número de 0 a 2." % linha)
                continue
            break

        while True:
            coluna = int(input("Digite o número da coluna que deseja: "))
            if coluna > 2:
                print("Valor %d inválido. Digite um número de 0 a 2." % coluna)
                continue
            break

        if grade[linha][coluna] is not None:
            print("Posição já tem valor. Informe outro valor.")
            continue
        break

    while True:
        valor = input("X ou O? ")
        if valor != "x" and valor != "o":
            print("Valor %s inválido. Digite X ou O." % valor)
            continue
        break

    grade[linha][coluna] = valor
    imprimir_grade(grade)

    ganhador = verificar_vitoria()
    if ganhador:
        print("Parabéns você venceu!")
        break



