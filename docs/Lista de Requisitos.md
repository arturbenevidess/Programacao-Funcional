## *Documento de Requisitos da Calculadora Científica Avançada*

### *1. Requisitos Funcionais*
Os *requisitos funcionais* descrevem as funcionalidades que o sistema deve possuir. Abaixo estão as funcionalidades previstas no sistema, com a respectiva identificação de como elas foram implementadas no código:

#### *RF01 - Cálculo de Potências e Raízes*
- *Descrição:* O sistema deve permitir ao usuário calcular potências e raízes de números, com a opção de passar uma função de alta ordem que modifica o resultado.
- *Implementação:* 
  - Função calcular_potencia_ou_raiz()
  - Função de alta ordem permite modificação do resultado com uma função como argumento (ex: lambda x: round(x, 2)).
  
#### *RF02 - Cálculo de Funções Trigonométricas*
- *Descrição:* O sistema deve permitir o cálculo de seno, cosseno e tangente utilizando séries de Taylor, com suporte para ângulos em graus e radianos.
- *Implementação:* 
  - Função calcular_trigonometria() 
  - Implementada com *list comprehension* para cálculo do seno e cosseno.
  
#### *RF03 - Realização de Operações Matemáticas Básicas*
- *Descrição:* O sistema deve permitir ao usuário realizar operações de soma, subtração, multiplicação e divisão entre dois números, com suporte para tratamento de divisões por zero.
- *Implementação:* 
  - Função operacoes_basicas()
  - Uso de *função lambda* para executar operações de forma anônima e compacta.

#### *RF04 - Cálculo de Logaritmos*
- *Descrição:* O sistema deve calcular logaritmos de um número em qualquer base fornecida pelo usuário, ou usar a base 2 como padrão.
- *Implementação:* 
  - Função calcular_logaritmo()
  - Função pura que utiliza o math.log para cálculos precisos de logaritmo.

#### *RF05 - Resolução de Equações de Segundo Grau*
- *Descrição:* O sistema deve resolver equações do segundo grau na forma \( ax^2 + bx + c = 0 \), retornando as raízes reais (ou indicando que não existem raízes reais).
- *Implementação:* 
  - Função resolver_equacao_segundo_grau()
  - Uso de *closure* para encapsular o cálculo das raízes, reutilizando o valor do discriminante calculado.

#### *RF06 - Soma de uma Lista de Números*
- *Descrição:* O sistema deve permitir somar todos os elementos de uma lista de números.
- *Implementação:* 
  - Função somar_lista_numeros()
  - Implementada com o uso da *função de alta ordem* reduce() do módulo functools.

#### *RF07 - Histórico de Operações*
- *Descrição:* O sistema deve manter um histórico das operações matemáticas básicas realizadas pelo usuário.
- *Implementação:* 
  - Função operacoes_basicas() salva o histórico com a função salvar_no_historico(), armazenando as operações e resultados realizados.

### *2. Requisitos Não Funcionais*
Os *requisitos não funcionais* descrevem atributos de qualidade, desempenho, segurança, entre outros, que o sistema deve satisfazer. Abaixo estão os requisitos não funcionais do sistema e como eles estão sendo implementados.

#### *RNF01 - Eficiência de Cálculo*
- *Descrição:* O sistema deve ser eficiente ao realizar cálculos, especialmente cálculos de potências, raízes e trigonometria.
- *Implementação:* 
  - Uso de *séries de Taylor* para aproximação de funções trigonométricas.
  - Funções puras e *list comprehension* são utilizadas para tornar as funções mais otimizadas.

#### *RNF02 - Precisão dos Resultados*
- *Descrição:* O sistema deve garantir alta precisão nos cálculos realizados, com arredondamento opcional conforme a necessidade do usuário.
- *Implementação:* 
  - As funções utilizam round() para garantir precisão nas casas decimais. O usuário pode passar funções de arredondamento como argumento nas funções de alta ordem.

#### *RNF03 - Tratamento de Erros*
- *Descrição:* O sistema deve ser robusto e tratar erros como divisão por zero, raiz de índice inválido, ou operações com números inválidos.
- *Implementação:* 
  - Exceções como ValueError e verificações preventivas são aplicadas nas funções de cálculo (ex: divisão por zero, índice de raiz igual a zero).

#### *RNF04 - Manutenibilidade*
- *Descrição:* O código deve ser modular e fácil de manter, permitindo futuras expansões e adição de novas funcionalidades.
- *Implementação:* 
  - O código está organizado em funções independentes e modulares, com clara separação de responsabilidades. Conceitos como funções puras, funções de alta ordem, closures, e lambda são usados para manter o código enxuto e flexível.

#### *RNF05 - Simplicidade e Facilidade de Uso*
- *Descrição:* O sistema deve ser simples de usar e oferecer uma interface clara para os usuários realizarem suas operações.
- *Implementação:* 
  - A função main() exibe um menu claro para que o usuário escolha a operação desejada. Mensagens de erro amigáveis são mostradas quando o usuário insere valores incorretos.

#### *RNF06 - Portabilidade*
- *Descrição:* O sistema deve ser portável e executável em diferentes ambientes, como terminal ou IDEs padrão.
- *Implementação:* 
  - O sistema foi escrito em Python, utilizando apenas bibliotecas padrão, garantindo que ele possa ser executado em qualquer ambiente que suporte Python.

#### *Observações*
- Foi utilizado IA para facilitar a formatação dos documentos.
