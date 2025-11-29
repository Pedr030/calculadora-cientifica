import operacoes
from utils import quebra_linha, mostraresultado, ocultar_ponto_flutuante

while True:
    print('0 - Sair\n1 - Operações Básicas\n2 - Operações Científicas')
    cmd = int(input('Insira o comando desejado: '))
    quebra_linha()
    if cmd == 1:
        n1 = float(input('Insira o primeiro número: '))
        n2 = float(input('Insira o segundo número: '))
        sinal = input('Insira o sinal da operação: ')
        resultado = ocultar_ponto_flutuante(operacoes.operacoes_basicas(n1, n2, sinal))
        quebra_linha()
        mostraresultado(resultado)
        quebra_linha()
    elif cmd == 2:
        n1 = float(input('Insira o primeiro número: '))
        n2 = float(input('Insira o segundo número: '))
        print('Sinal da operação: potencia, raiz, log')
        sinal = input('Insira o sinal da operação: ')
        resultado = ocultar_ponto_flutuante(operacoes.operacoes_cientificas(n1, n2, sinal))
        quebra_linha()
        mostraresultado(resultado)
        quebra_linha()
    elif cmd == 0:
        break
    else:
        print('Comando inválido')
        quebra_linha()

print('Programa Encerrado\nAté Mais!')