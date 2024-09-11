# Trabalho de Programação Funcional

## Calculadora Científica Avançada

Cada aluno foi responsável por uma função matemática específica, e o programa principal combina todas as funções para resolver uma equação complexa:

- **Função para calcular potências e raízes.**
- **Função para trigonometria (seno, cosseno, tangente).**
- **Função para operações básicas (soma, subtração, multiplicação, divisão).**
- **Função para logaritmos e exponenciais.**
- **Função que combina todas as outras para resolver uma equação completa** (ex: resolver uma equação de segundo grau).

---

### **Artur Benevides: Funções de Potência e Raiz + Funções de Trigonometria**

Minha responsabilidade no projeto foi implementar as funções para o cálculo de potências e raízes. No cálculo da potência, usei laços para iterar e multiplicar o número base pelo número de vezes correspondente ao expoente. Para expoentes negativos, utilizei uma lógica inversa, dividindo o resultado pela base a cada iteração.

A parte mais desafiadora foi a implementação da função de raiz, onde apliquei o método de aproximação de **Newton-Raphson**. Esse método permite encontrar uma aproximação razoável para raízes n-ésimas sem depender de funções prontas de bibliotecas. A função foi otimizada para precisão e converge em torno de uma margem de erro mínima, definida como `0.001`.

Além disso, incluí tratamento de erros para entradas inválidas, como números negativos em raízes pares. Também implementei as funções de seno, cosseno e tangente utilizando séries de **Taylor**. Este método é particularmente útil para calcular aproximações de funções trigonométricas. Consegui calcular essas funções com precisão ao incluir 10 termos na série de Taylor, garantindo uma boa aproximação para ângulos em radianos.

A conversão de graus para radianos também foi feita manualmente. Essa função agora consegue calcular as três funções trigonométricas simultaneamente e retorna os resultados arredondados. Além disso, implementei uma função auxiliar para calcular fatoriais, já que a série de Taylor depende deles.

---

### **Shirley Dias: Operações Matemáticas Básicas com Histórico**

Minha contribuição foi desenvolver as operações básicas de matemática (soma, subtração, multiplicação e divisão) de maneira manual. Além das operações simples, adicionei um sistema de **histórico** que armazena todas as operações realizadas com os respectivos resultados.

O foco da implementação foi garantir que, além de executar operações, o código fosse capaz de registrar e recuperar os cálculos feitos anteriormente. Também incluí uma lógica de tratamento para evitar divisão por zero e fornecer uma mensagem de erro adequada para essa situação.

---

### **Brendo Mendes: Cálculo de Logaritmos**

Minha responsabilidade foi criar uma função que calcula logaritmos. Para isso, implementei uma função de logaritmo com **mudança de base**. Utilizei uma abordagem binária, iterando sobre o valor e ajustando-o de acordo com a base escolhida.

A função também possui tratamento de entradas inválidas, como números negativos ou base incorreta. O logaritmo base 2 foi escolhido como padrão, mas a função permite que o usuário especifique outras bases. A aproximação se baseia no método de redução sucessiva, garantindo precisão satisfatória.

---

### **Giselle Bezerra: Resolução de Equações de Segundo Grau**

Fiquei encarregada de implementar a função principal do projeto, que resolve equações de segundo grau. Para isso, integrei as funções dos colegas, como o cálculo de potências e a multiplicação, para calcular o discriminante da equação e determinar as raízes.

A função trata três casos possíveis:
- Quando **não há raízes reais** (discriminante negativo),
- Quando há **uma raiz** (discriminante igual a zero),
- Quando existem **duas raízes reais distintas** (discriminante positivo).

Além disso, inclui tratamento de erros para entradas inválidas, como quando o coeficiente 'a' é zero, o que descaracterizaria a equação de segundo grau.

---

## **Conclusão**

Neste projeto, trabalhamos juntos para desenvolver uma **calculadora científica avançada**. Cada integrante foi responsável por uma parte essencial do código, garantindo que todas as operações fossem implementadas de forma manual e funcional.

O desafio foi grande, principalmente na implementação de algoritmos matemáticos complexos como **raízes, trigonometria e logaritmos**, mas conseguimos entregar um código robusto, com tratamento de erros e funcionalidades completas.
