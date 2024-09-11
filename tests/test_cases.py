
import unittest
from src.Trabalho_Programacao_Funcional import calcular_potencia_ou_raiz, calcular_trigonometria, operacoes_basicas

class TestFuncoesMatematicas(unittest.TestCase):

    # Caso de Teste 01 - Cálculo de Potências e Raízes
    def test_calculo_potencia(self):
        resultado = calcular_potencia_ou_raiz(2, 3, 'potencia')
        self.assertEqual(resultado, 8)

    def test_calculo_raiz(self):
        resultado = calcular_potencia_ou_raiz(16, 2, 'raiz')
        self.assertEqual(resultado, 4)

    def test_calculo_potencia_zero(self):
        resultado = calcular_potencia_ou_raiz(0, 3, 'potencia')
        self.assertEqual(resultado, 0)

    def test_raiz_indice_zero(self):
        resultado = calcular_potencia_ou_raiz(16, 0, 'raiz')
        self.assertEqual(resultado, "Erro: O índice da raiz não pode ser zero.")

    def test_raiz_numero_negativo(self):
        resultado = calcular_potencia_ou_raiz(-16, 2, 'raiz')
        self.assertTrue("Erro" in resultado)

    # Caso de Teste 02 - Cálculo de Funções Trigonométricas
    def test_calculo_trigonometria_graus(self):
        resultados_trig = calcular_trigonometria(30, 'graus')
        self.assertAlmostEqual(resultados_trig['seno'], 0.5, places=2)
        self.assertAlmostEqual(resultados_trig['cosseno'], 0.86603, places=2)
        self.assertAlmostEqual(resultados_trig['tangente'], 0.57735, places=2)

    def test_calculo_trigonometria_radianos(self):
        resultados_trig = calcular_trigonometria(1, 'radianos')
        self.assertAlmostEqual(resultados_trig['seno'], 0.84147, places=2)
        self.assertAlmostEqual(resultados_trig['cosseno'], 0.5403, places=2)
        self.assertAlmostEqual(resultados_trig['tangente'], 1.55741, places=2)

    def test_calculo_trigonometria_angulo_zero(self):
        resultados_trig = calcular_trigonometria(0, 'graus')
        self.assertEqual(resultados_trig['seno'], 0)
        self.assertEqual(resultados_trig['cosseno'], 1)
        self.assertEqual(resultados_trig['tangente'], 0)

    # Caso de Teste 03 - Operações Matemáticas Básicas
    def test_operacoes_soma(self):
        resultado, _ = operacoes_basicas(5, 3, 'soma')
        self.assertEqual(resultado, 8)

    def test_operacoes_divisao(self):
        resultado, _ = operacoes_basicas(9, 3, 'divisao')
        self.assertEqual(resultado, 3)

    def test_divisao_por_zero(self):
        resultado, _ = operacoes_basicas(10, 0, 'divisao')
        self.assertEqual(resultado, "Erro: Divisão por zero!")

    def test_operacao_invalida(self):
        resultado = operacoes_basicas(5, 2, 'multiplicacaoo')
        self.assertEqual(resultado, "Operação inválida!")

if __name__ == '__main__':
    unittest.main()
