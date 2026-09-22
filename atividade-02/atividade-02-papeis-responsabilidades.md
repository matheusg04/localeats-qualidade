# Atividade 2 - Organização da Qualidade no LocalEats

**Aluno:** Matheus Gante Pinto
**Unidade Curricular:** Qualidade de Software

## 1. Diagnóstico da situação

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| As funcionalidades chegam aos usuários com defeitos. | Os usuários podem encontrar problemas durante o uso do sistema. |
| Não estão claros os critérios para considerar uma funcionalidade pronta. | Uma funcionalidade pode ser disponibilizada sem estar realmente preparada. |
| Alguns integrantes acreditam que somente o QA deve testar. | A qualidade fica concentrada em uma pessoa e os demais integrantes podem deixar de participar da identificação de problemas. |

### A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA?

Não. A qualidade deve ser uma responsabilidade compartilhada entre os diferentes papéis da equipe. O QA tem uma participação importante nos testes e na qualidade, mas desenvolvedores, liderança e responsáveis pelo produto também precisam participar para evitar problemas e melhorar o resultado final.

---

## 2. Papéis e competências

| Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|
| Desenvolvedor | Implementar funcionalidades, corrigir defeitos, revisar código e criar testes unitários. | Programação, Git, testes unitários e conhecimento da aplicação. | Organização, comunicação e trabalho em equipe. |
| QA / Analista de qualidade | Planejar testes, executar testes, registrar defeitos e acompanhar os resultados. | Técnicas de teste, elaboração de casos de teste e registro de defeitos. | Atenção aos detalhes, organização e pensamento crítico. |
| Responsável pelo produto | Definir necessidades e critérios de aceitação e participar da priorização dos defeitos. | Conhecimento do produto e dos requisitos. | Comunicação, organização e tomada de decisão. |
| Liderança técnica | Apoiar decisões técnicas, revisar soluções e ajudar a garantir padrões de desenvolvimento. | Arquitetura, programação, revisão de código e conhecimento técnico do projeto. | Liderança, comunicação e colaboração. |

---

## 3. Matriz RACI

**R = Responsável pela execução**  
**A = Aprovador / responsável pelo resultado final**  
**C = Consultado**  
**I = Informado**

| Atividade de qualidade | Responsável pelo produto | Desenvolvedor | QA | Liderança técnica |
|---|---|---|---|---|
| Definir critérios de aceitação | A/R | C | C | I |
| Revisar requisitos | A | R | C | I |
| Implementar a funcionalidade | I | A/R | C | C |
| Revisar o código | I | R | C | A |
| Criar testes unitários | I | A/R | C | I |
| Planejar e executar testes do sistema | I | C | A/R | C |
| Registrar e acompanhar defeitos | I | C | A/R | I |
| Priorizar a correção dos defeitos | A/R | C | C | I |
| Aprovar a disponibilização da versão | A | C | C | R |

---

## 4. Lacuna ou conflito encontrado

Uma possível lacuna é a concentração das atividades de teste somente no QA. Mesmo que o QA seja responsável pelo planejamento e execução dos testes do sistema, os desenvolvedores também precisam participar da qualidade por meio de testes unitários, revisão de código e correção dos defeitos.

---

## 5. Práticas recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Revisão de código antes da disponibilização | Reduz a chance de defeitos chegarem aos usuários. | Desenvolvedor e liderança técnica. |
| Registro e acompanhamento dos defeitos em um fluxo único | Evita que problemas sejam esquecidos ou fiquem sem acompanhamento. | QA, desenvolvedor e responsável pelo produto. |

---

## Uso de inteligência artificial

**Ferramenta utilizada:** ChatGPT.

**Como foi utilizada:** Foi utilizada como apoio para organizar os papéis, responsabilidades e a matriz RACI.

**Como as respostas foram verificadas:** As sugestões foram comparadas com as definições de RACI e com os problemas apresentados no enunciado da atividade.
