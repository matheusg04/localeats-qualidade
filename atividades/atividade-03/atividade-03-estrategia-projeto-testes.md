# Atividade 3 - Estratégia e Projeto de Testes do LocalEats

**Aluno:** Matheus Gante Pinto
**Unidade Curricular:** Qualidade de Software

## 1. Plano simplificado de testes

### 1.1 Objetivo dos testes

Verificar se o usuário consegue realizar um pedido pelo LocalEats seguindo o fluxo esperado e se o sistema impede ou trata situações em que as condições necessárias para o pedido não foram atendidas.

### 1.2 Escopo

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Matheus | Fazer pedido | Seleção de prato, realização do pedido e comportamento em situações em que o usuário não está autenticado ou não possui item selecionado. |

| Funcionalidade não incluída | Justificativa |
|---|---|
| Cadastro de usuário | Não faz parte diretamente do fluxo escolhido para os testes de realização do pedido. |

### 1.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Nível de teste | Sistema | O fluxo será analisado pela interface do LocalEats, considerando o processo de pedido. |
| Tipo de teste | Funcional | O objetivo é verificar o comportamento da funcionalidade e suas regras. |
| Perspectiva | Caixa-preta | Serão analisadas as entradas e os resultados observáveis, sem analisar o código. |
| Técnica de teste | Tabela de decisão | A realização do pedido depende de diferentes condições, como autenticação e existência de um item selecionado. |

### 1.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | LocalEats disponível no navegador e conexão com a internet. |
| Responsável pelo planejamento | Matheus |
| Responsável pela especificação dos casos | Matheus |
| Responsável pela futura execução | Matheus |

### 1.5 Critérios

| Critério | Definição |
|---|---|
| Entrada | Aplicação disponível, usuário cadastrado e restaurante com pratos disponíveis. |
| Saída | Todos os casos planejados executados e resultados registrados. |
| Suspensão | Aplicação indisponível ou impossibilidade de acessar as funcionalidades necessárias para os testes. |

---

# 2. Riscos e técnicas de teste

## 2.1 Análise dos riscos

| ID | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|---|---|---|
| R01 | Fazer pedido | O sistema permitir tentar realizar um pedido sem que o usuário esteja autenticado. | O fluxo de pedido pode ser realizado de forma incorreta ou gerar comportamento inesperado. | Média | Alta | Alta | A autenticação é uma condição importante para identificar o usuário e seu pedido. |
| R02 | Fazer pedido | O sistema permitir continuar o pedido sem selecionar um prato. | O usuário poderia tentar finalizar um pedido sem nenhum item. | Baixa | Alta | Média | A seleção de pelo menos um prato é necessária para que exista um pedido. |

---

## 2.2 Aplicação da técnica

### Técnica escolhida: Tabela de decisão

**Funcionalidade:** Fazer pedido

**Riscos relacionados:** R01 e R02

### Por que a técnica foi escolhida?

A tabela de decisão é adequada porque o comportamento do pedido depende da combinação de algumas condições. Podemos verificar, por exemplo, se o usuário está autenticado e se existe um prato selecionado antes de permitir a realização do pedido.

### Aplicação da técnica

| Regra | Usuário autenticado? | Prato selecionado? | Resultado esperado |
|---|---|---|---|
| 1 | Sim | Sim | Permitir a realização do pedido. |
| 2 | Sim | Não | Impedir o pedido e exigir a seleção de um prato. |
| 3 | Não | Sim | Solicitar autenticação antes de continuar. |
| 4 | Não | Não | Solicitar autenticação e não permitir a realização do pedido. |

**Casos derivados:** CT01, CT02 e CT03.

---

# 3. Casos de teste

## CT01 - Realizar pedido com usuário autenticado e prato selecionado

**Integrante responsável:** Matheus

**Funcionalidade:** Fazer pedido

**Risco relacionado:** R01

**Técnica utilizada:** Tabela de decisão

**Pré-condição:** Usuário autenticado e restaurante com pratos disponíveis.

**Dados de entrada:** Usuário válido e um prato disponível.

**Passos:**
1. Acessar o LocalEats.
2. Fazer login.
3. Acessar um restaurante.
4. Selecionar um prato.
5. Finalizar o pedido.

**Resultado esperado:** O sistema deve permitir a realização do pedido e apresentar a confirmação da operação.

---

## CT02 - Impedir pedido sem prato selecionado

**Integrante responsável:** Matheus

**Funcionalidade:** Fazer pedido

**Risco relacionado:** R02

**Técnica utilizada:** Tabela de decisão

**Pré-condição:** Usuário autenticado e restaurante disponível.

**Dados de entrada:** Nenhum prato selecionado.

**Passos:**
1. Acessar o LocalEats.
2. Fazer login.
3. Acessar um restaurante.
4. Não selecionar nenhum prato.
5. Tentar continuar o processo de pedido.

**Resultado esperado:** O sistema não deve permitir a realização do pedido sem que pelo menos um prato seja selecionado.

---

## CT03 - Impedir pedido sem autenticação

**Integrante responsável:** Matheus

**Funcionalidade:** Fazer pedido

**Risco relacionado:** R01

**Técnica utilizada:** Tabela de decisão

**Pré-condição:** Usuário não autenticado.

**Dados de entrada:** Restaurante e prato disponível.

**Passos:**
1. Acessar o LocalEats sem estar autenticado.
2. Acessar um restaurante, caso seja permitido.
3. Selecionar um prato, caso seja permitido.
4. Tentar realizar o pedido.

**Resultado esperado:** O sistema deve solicitar a autenticação do usuário e não permitir a conclusão do pedido sem login.

---

# 4. Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Matheus | Fazer pedido | R01 - Pedido sem autenticação | Tabela de decisão | CT01 e CT03 |
| Matheus | Fazer pedido | R02 - Pedido sem prato selecionado | Tabela de decisão | CT02 |

---

## Uso de inteligência artificial

**Ferramenta utilizada:** ChatGPT.

**Como foi utilizada:** Foi utilizada como apoio para sugerir riscos, comparar técnicas de teste, organizar os casos de teste e revisar a clareza do documento.

**Como as respostas foram verificadas:** As decisões foram comparadas com o enunciado da atividade e com as situações observadas diretamente no LocalEats.
