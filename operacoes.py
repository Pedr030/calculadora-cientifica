import math

def operacoes_basicas(n1, n2, sinal):
    if sinal == "+":
        return n1 + n2
    elif sinal == "-":
        return n1 - n2
    elif sinal == "*":
        return n1 * n2
    elif sinal == "/":
        return n1 / n2
    else:
        return "Sinal inválido"

def operacoes_cientificas(n1, n2, sinal):
    if sinal == "potencia":
        return math.pow(n1, n2)
    elif sinal == "raiz":
        return math.sqrt(n1)
    elif sinal == "log":
        return math.log(n1, n2)
    else:
        return "Sinal inválido"

