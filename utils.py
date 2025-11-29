def quebra_linha():
    print("________________________________")

def mostraresultado(resultado):
    print("Resultado: ", resultado)

def ocultar_ponto_flutuante(numero):
    if numero.is_integer():
        return int(numero)
    else:
        return numero