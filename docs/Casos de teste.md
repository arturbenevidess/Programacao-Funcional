### **Caso de Teste 01 - Cálculo de Potências e Raízes**

#### **Cenário Normal**
- **Entrada:** número = 2, expoente = 3, operação = 'potencia'
- **Saída esperada:** 8
- **Descrição:** Testa o cálculo de 2 elevado a 3.

- **Entrada:** número = 16, expoente = 2, operação = 'raiz'
- **Saída esperada:** 4
- **Descrição:** Testa o cálculo da raiz quadrada de 16.

#### **Cenário Limite**
- **Entrada:** número = 0, expoente = 3, operação = 'potencia'
- **Saída esperada:** 0
- **Descrição:** Testa o comportamento de 0 elevado a qualquer potência.

- **Entrada:** número = 16, expoente = 0, operação = 'raiz'
- **Saída esperada:** Erro: O índice da raiz não pode ser zero.
- **Descrição:** Testa erro ao calcular a raiz de índice zero.

#### **Cenário de Erro**
- **Entrada:** número = -16, expoente = 2, operação = 'raiz'
- **Saída esperada:** Erro
- **Descrição:** Testa o cálculo de raiz de um número negativo com expoente par (sem raízes reais).

---

### **Caso de Teste 02 - Cálculo de Funções Trigonométricas**

#### **Cenário Normal**
- **Entrada:** angulo = 30, unidade = 'graus'
- **Saída esperada:** Seno: 0.5, Cosseno: 0.86603, Tangente: 0.57735
- **Descrição:** Testa o cálculo do seno, cosseno e tangente para 30 graus.

- **Entrada:** angulo = 1, unidade = 'radianos'
- **Saída esperada:** Seno: 0.84147, Cosseno: 0.5403, Tangente: 1.55741
- **Descrição:** Testa o cálculo do seno, cosseno e tangente para 1 radiano.

#### **Cenário Limite**
- **Entrada:** angulo = 0, unidade = 'graus'
- **Saída esperada:** Seno: 0, Cosseno: 1, Tangente: 0
- **Descrição:** Testa o cálculo de funções trigonométricas para ângulo 0.

#### **Cenário de Erro**
- **Entrada:** angulo = 'texto', unidade = 'graus'
- **Saída esperada:** Erro de tipo
- **Descrição:** Testa erro ao passar valor não numérico como ângulo.

---

### **Caso de Teste 03 - Operações Matemáticas Básicas**

#### **Cenário Normal**
- **Entrada:** a = 5, b = 3, operação = 'soma'
- **Saída esperada:** 8
- **Descrição:** Testa a soma de dois números.

- **Entrada:** a = 9, b = 3, operação = 'divisao'
- **Saída esperada:** 3
- **Descrição:** Testa a divisão de dois números.

#### **Cenário Limite**
- **Entrada:** a = 10, b = 0, operação = 'divisao'
- **Saída esperada:** Erro: Divisão por zero!
- **Descrição:** Testa divisão por zero.

#### **Cenário de Erro**
- **Entrada:** a = 5, b = 2, operação = 'multiplicacaoo' (erro de digitação)
- **Saída esperada:** Operação inválida!
- **Descrição:** Testa o comportamento quando o nome da operação é digitado incorretamente.

---

### **Caso de Teste 04 - Cálculo de Logaritmo**

#### **Cenário Normal**
- **Entrada:** número = 16, base = 2
- **Saída esperada:** 4
- **Descrição:** Testa o cálculo do logaritmo de 16 na base 2.

- **Entrada:** número = 1000, base = 10
- **Saída esperada:** 3
- **Descrição:** Testa o cálculo do logaritmo de 1000 na base 10.

#### **Cenário Limite**
- **Entrada:** número = 1, base = 10
- **Saída esperada:** 0
- **Descrição:** Testa o cálculo do logaritmo de 1, que deve sempre resultar em 0.

#### **Cenário de Erro**
- **Entrada:** número = -16, base = 2
- **Saída esperada:** Erro: O número para logaritmo deve ser positivo.
- **Descrição:** Testa o comportamento ao calcular logaritmo de número negativo.

---

### **Caso de Teste 05 - Resolução de Equações de Segundo Grau**

#### **Cenário Normal**
- **Entrada:** a = 1, b = -3, c = 2
- **Saída esperada:** Raízes reais: 2.0 e 1.0
- **Descrição:** Testa o cálculo das raízes reais de uma equação com discriminante positivo.

- **Entrada:** a = 1, b = 2, c = 1
- **Saída esperada:** Uma raiz real: -1.0
- **Descrição:** Testa o cálculo de uma equação com discriminante zero.

#### **Cenário Limite**
- **Entrada:** a = 1, b = 0, c = -1
- **Saída esperada:** Raízes reais: 1.0 e -1.0
- **Descrição:** Testa o cálculo de uma equação onde b é 0.

#### **Cenário de Erro**
- **Entrada:** a = 0, b = 3, c = 2
- **Saída esperada:** Erro: O coeficiente 'a' deve ser diferente de zero para ser uma equação de segundo grau.
- **Descrição:** Testa erro ao passar 0 para o coeficiente 'a', que invalidaria a equação de segundo grau.

---

### **Caso de Teste 06 - Soma de uma Lista de Números**

#### **Cenário Normal**
- **Entrada:** lista = [1, 2, 3, 4, 5]
- **Saída esperada:** 15
- **Descrição:** Testa a soma dos números de uma lista usando a função `reduce`.

#### **Cenário Limite**
- **Entrada:** lista = [0, 0, 0, 0]
- **Saída esperada:** 0
- **Descrição:** Testa a soma de uma lista com todos os elementos sendo zero.

#### **Cenário de Erro**
- **Entrada:** lista = [1, 2, 'texto', 4]
- **Saída esperada:** Erro de tipo
- **Descrição:** Testa erro ao passar um elemento não numérico na lista.

---

### **Execução e Verificação**

Esses casos de teste podem ser executados manualmente ou, preferencialmente, automatizados utilizando frameworks de testes como `unittest` ou `pytest` em Python. Eles garantem que todas as funcionalidades do sistema sejam cobertas e tratam tanto os cenários de uso comum quanto os casos limites e de erro.

Casos de teste desenhados por: Shirley Barbosa, Brendo Mendes e Artur Benevides
