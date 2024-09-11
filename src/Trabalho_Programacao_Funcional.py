import math
from functools import reduce

# Artur Benevides: Função para calcular potências e raízes com função de alta ordem e função para trigonometria (usando séries de Taylor e list comprehension)
def calcular_potencia_ou_raiz(numero, expoente, operacao='potencia', funcao_alta_ordem=None):
    try:
        if operacao == 'potencia':
            resultado = numero ** expoente  # Função pura
        elif operacao == 'raiz':
            if expoente == 0:
                raise ValueError("O índice da raiz não pode ser zero.")
            resultado = numero ** (1/expoente)  # Função pura
        else:
            raise ValueError("Operação inválida. Escolha 'potencia' ou 'raiz'.")

        # Função de alta ordem
        if funcao_alta_ordem:
            return funcao_alta_ordem(resultado)
        return round(resultado, 5)
    
    except ValueError as ve:
        return f"Erro: {ve}"
    except Exception:
        return "Erro: Verifique se ambos os valores são números."


def calcular_trigonometria(angulo, unidade='graus'):
    if unidade == 'graus':
        angulo = math.radians(angulo)

    # List comprehension
    def seno(x):
        return sum([((-1)**i * x**(2*i+1)) / math.factorial(2*i+1) for i in range(10)])

    def cosseno(x):
        return sum([((-1)**i * x**(2*i)) / math.factorial(2*i) for i in range(10)])

    # Tangente utilizando as funções puras seno e cosseno
    def tangente(x):
        return seno(x) / cosseno(x)

    return {
        'seno': round(seno(angulo), 5),
        'cosseno': round(cosseno(angulo), 5),
        'tangente': round(tangente(angulo), 5)
    }

# Shirley Dias: Função para operações matemáticas básicas com lambda
def operacoes_basicas(a, b, operacao):
    historico = []

    def salvar_no_historico(op, res):
        historico.append(f"Operação: {op}, Resultado: {res}")

    # Funções lambda para operações básicas
    operacoes = {
        'soma': lambda x, y: x + y,
        'subtracao': lambda x, y: x - y,
        'multiplicacao': lambda x, y: x * y,
        'divisao': lambda x, y: x / y if y != 0 else "Erro: Divisão por zero!"
    }

    if operacao in operacoes:
        resultado = operacoes[operacao](a, b) 
        salvar_no_historico(operacao, resultado)
    else:
        return "Operação inválida!"

    return resultado, historico

# Brendo Mendes: Função para calcular logaritmo (Função pura)
def calcular_logaritmo(numero, base=None):
    if numero <= 0:
        return "Erro: O número para logaritmo deve ser positivo."
    
    if base is None:
        base = 2  # Default base é 2

    return f"Logaritmo de {numero} na base {base} é {round(math.log(numero, base), 5)}"

# Giselle Bezerra: Função principal que resolve equações de segundo grau com closure e reduce
def resolver_equacao_segundo_grau(a, b, c):
    if a == 0:
        return "Erro: O coeficiente 'a' deve ser diferente de zero para ser uma equação de segundo grau."
    
    discriminante = b**2 - 4 * a * c 

    def calcular_raizes(discriminante):
        if discriminante < 0:
            return "A equação não possui raízes reais."
        elif discriminante == 0:
            raiz = -b / (2 * a)
            return f"A equação tem uma raiz real: {round(raiz, 5)}"
        else:
            raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
            raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
            return f"As raízes reais são: {round(raiz1, 5)} e {round(raiz2, 5)}"

    # Função de alta ordem:
    return calcular_raizes(discriminante)

def somar_lista_numeros(lista):
    return reduce(lambda x, y: x + y, lista) 


# Função main que integra todas as funcionalidades
def main():
    print("Bem-vindo à Calculadora Científica Avançada!")
    print("Esta calculadora realiza as seguintes operações:")
    print("1. Cálculo de potências e raízes")
    print("2. Funções trigonométricas (seno, cosseno, tangente)")
    print("3. Operações matemáticas básicas (soma, subtração, multiplicação e divisão)")
    print("4. Cálculo de logaritmos")
    print("5. Resolução de equações de segundo grau")
    print("6. Somar lista de números usando reduce")

    while True:
        print("\nEscolha uma operação:")
        print("1 - Potência ou Raiz")
        print("2 - Trigonometria")
        print("3 - Operações Básicas")
        print("4 - Logaritmo")
        print("5 - Resolver Equação de Segundo Grau")
        print("6 - Somar lista de números")
        print("7 - Sair")
        opcao = input("Digite o número da operação que deseja realizar: ")

        if opcao == '1':
            numero = float(input("Digite o número: "))
            expoente = int(input("Digite o expoente (para raízes, digite o índice da raiz): "))
            operacao = input("Deseja calcular 'potencia' ou 'raiz'? ").lower()

            # Função de alta ordem para arredondar o resultado
            resultado = calcular_potencia_ou_raiz(numero, expoente, operacao, funcao_alta_ordem=lambda x: round(x, 2))
            print(f"Resultado: {resultado}")

        elif opcao == '2':
            angulo = float(input("Digite o ângulo: "))
            unidade = input("O ângulo está em 'graus' ou 'radianos'? ").lower()
            resultados_trig = calcular_trigonometria(angulo, unidade)
            print(f"Seno: {resultados_trig['seno']}, Cosseno: {resultados_trig['cosseno']}, Tangente: {resultados_trig['tangente']}")

        elif opcao == '3':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação ('soma', 'subtracao', 'multiplicacao', 'divisao'): ").lower()
            resultado, historico = operacoes_basicas(a, b, operacao)
            print(f"Resultado: {resultado}")
            print("Histórico de operações")
